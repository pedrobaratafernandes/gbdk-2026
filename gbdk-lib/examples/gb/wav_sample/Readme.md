
Demonstration of how to convert and play wav sample files

Included wav audio files are in the public domain

## Conversion of samples:
### Linux:
  - `utils/cvtsample.py sndrec/cowbell_8bit_pcm_unsigned.wav sample1 C > src/sample_data_1.h`
  - `utils/cvtsample.py sndrec/risset_drum_8bit_pcm_unsigned.wav sample2 C > src/sample_data_2.h`

### Windows
  - `python .\utils\cvtsample_windows.py ..\sndrec\cowbell_8bit_pcm_unsigned.wav sample1 ..\src\sample_data_1.h`
  - `python .\utils\cvtsample_windows.py ..\sndrec\risset_drum_8bit_pcm_unsigned.wav sample2 ..\src\sample_data_2.h`