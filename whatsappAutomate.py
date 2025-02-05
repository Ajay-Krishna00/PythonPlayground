import pywhatkit as kit
import time

for i in range(0, 24):
  # names=["Anusha","Aravind","Devika","Althaf","Fida","Gaya","Harishanker","Hridya","Anand","Meenakshi","Minnu","Bilal","Nita Teresa","Paul Varghese","Pavithra","Sandra","Tina","Varsha"]
  # ph=["+918281613647","+919061089891","+919037435133","+919778739309","+918590310611","+919526924864","+919971815921","+918547085922","+917736010339","+917994149329","+918289850102","+918921136841","+918848919364","+918304039990","+916282268903","+919074602051","+918590240366","+917306326537"]
  
  names=["Adithya","Akil","Aleena","Alexander Matthew","Anandu","Anjali","Ann Maria ","Annu","Augustine","Bhavya","Devika","Elizabeth","Gyan","Kripa","Lakshmi","Lavanya","Laya","Malavika","Megha","Arshad","Parvathi","Priscilla Shibu","Swathi","Vaidehi"]
  ph=["+919746970380","+919632511881","+919074171877","+919446668448","+919744872696","+919207670434","+918547020455","+918289969811","+919645211014","+918281896821","+917356056724","+919744705712","+919995213205","+916282801350","+917306514846","+916235795605","+919446438309","+917306152610","+919446006726","+916282881055","+918301841695","+918304860420","+918431933728","+917994263324"]

  message=f"""Good Evening *{names[i]}*,\n I'm *Ajay Krishna D* from CS4C and I have been selected as a 2K27 Training Cell Intern. I'm excited to be a part of the team and look forward to learning and contributing under your guidance.\nExcited to bring my skills to the table and grow alongside the team!"""
  kit.sendwhatmsg_instantly(ph[i], message, wait_time=20, tab_close=True)
  time.sleep(15) 
