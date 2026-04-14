import sys, wave, struct

def convert(filename, varname, output_file=None):
    w = wave.open(filename, 'rb')
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = w.getparams()
    
    frames = w.readframes(nframes)
    out = []
    
    for i in range(0, len(frames), sampwidth):
        samp = struct.unpack_from('<h' if sampwidth == 2 else '<B', frames, i)[0]
        val = (samp >> 12) & 0x0F if sampwidth == 2 else (samp >> 4) & 0x0F
        out.append(val)
    
    lines = []
    lines.append(f"const UINT8 {varname}[] = {{")
    
    current_line = ""
    for i in range(0, len(out), 2):
        byte = (out[i] << 4) | (out[i+1] if i+1 < len(out) else 0)
        current_line += f"0x{byte:x},"
        if ((i//2+1) % 16) == 0:
            lines.append(current_line)
            current_line = ""
    
    if current_line:
        lines.append(current_line)
        
    lines.append("};")
    
    output_text = "\n".join(lines)
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8', newline='\n') as f:
            f.write(output_text)
        print(f"Ficheiro guardado em: {output_file}")
    else:
        print(output_text)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python cvtsample.py input.wav varname [output_file.h]")
    else:
        out_f = sys.argv[3] if len(sys.argv) > 3 else None
        convert(sys.argv[1], sys.argv[2], out_f)
