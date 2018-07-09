import requests, pydub
import wave
from io import BytesIO


#Normalize audio based on target dBFS
def match_target_amplitude(sound, target_dBFS):
  change_in_dBFS = target_dBFS - sound.dBFS
  return sound.apply_gain(change_in_dBFS)

#export audio to export_location  
def export_audio(audio_file, audio_name, file_type, export_location):
  audio_file.export(export_location+audio_name+'.'+file_type, format=file_type)

  
#add in ability to get any audio file from web -- type?
#Return pydub wave audio from website
def get_pydub_wave_fromweb(url):
  audio = requests.get(url)
  return pydub.AudioSegment.from_file(BytesIO(audio.content), 'wav')
  
def main():

  #Configuration
  file_type = 'wav'
  target_dBFS = -20.0
  #broken can't get the path to come out right...
  export_location = ""
  print export_location
  
  url1 = "https://affiliate.radionetworks.com/wp-content/plugins/common-core/af-download.php?file=kin_kan_pgms%2FSPKA10.wav"
  name1 = "KAN1"
  url2 = "https://affiliate.radionetworks.com/wp-content/plugins/common-core/af-download.php?file=kin_kan_pgms%2FSPKA11.wav"
  name2 = "KAN2"
  url3 = "https://affiliate.radionetworks.com/wp-content/plugins/common-core/af-download.php?file=kin_kan_pgms%2FSPKA12.wav"
  name3 = "KAN3"
  
  
  #Get Pydub Wave Audio File From Web
  cut1 = get_pydub_wave_fromweb(url1)
  cut2 = get_pydub_wave_fromweb(url2)
  cut3 = get_pydub_wave_fromweb(url3)
  
  
  #run function to look at dBFS and normalize audio to set dBFS
  cut1_normalized = match_target_amplitude(cut1, target_dBFS)
  cut2_normalized = match_target_amplitude(cut2, target_dBFS)
  cut3_normalized = match_target_amplitude(cut3, target_dBFS)
  
  
  #export audio to expoer_location
  export_audio(cut1_normalized,name1,file_type,export_location)
  export_audio(cut2_normalized,name2,file_type,export_location)
  export_audio(cut3_normalized,name3,file_type,export_location)


  
  
#Boiler Plate Default Main
if __name__ == '__main__':
  main()

  