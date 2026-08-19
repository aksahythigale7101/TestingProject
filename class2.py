
  
class SteamWr:
     
     # @staticmethod 
     # def writerData(str,mode):
     #   # with open(r"C:\Users\KIMAYA\Desktop\sample.txt",'w') as file: # w stands for write 
     #   with open("C:\\Users\\KIMAYA\\Desktop\\sample.txt", mode ) as file: # mode meanas pass mode then file write as per mode
     #       file.write(str)
     #       file.close()

      
       @staticmethod
       def readData():
           if os.path.exists(r"C:\Users\KIMAYA\Desktop\ABC.txt"):
               os.remove(r"C:\Users\KIMAYA\Desktop\ABC.txt")# remove means delete file -----,renane
               print("File exists")
           else:
               print("File not found")
           with open("C:\\Users\\KIMAYA\\Desktop\\sample.txt","r")as file:# "r" is read and r+ is read and write mode and photo.png-->rb is read binery
            reder=file.read()
            print(reder)
           #file.write("\nJava")# change mode is "r+"
          # lines = file.readlines()# data shows Audi \n,Bmw \n
          # print(lines) 
           # for line in file:
           #   print(line.strip()) # in this code strip remove \n
               
           
           # print(file.read(3))
           # file.seek(2) #Moves the file pointer.
           # print(file.read())
           # file.close()

            # print(file.tell())
            # file.read(4)
            # print(file.tell())
            # file.close()




           

           
            
         
          
          


# SteamWr.writerData("Audi\n","w")# "w" stands for create new file or clear old data and "x" mode create new file if file exits it give error
# SteamWr.writerData("BMW\n","a") # "a" stands for append data.
# SteamWr.writerData("Hyndai\n","a")
# SteamWr.writerData("Tata\n","a")
# SteamWr.writerData("Toyto\n","a")

# SteamWr.readData()
#SteamWr.writerData("Audi\nBMW\nMercedes\nTata")

#---------------------- MODULE-----------------------





# c=module1.Maths_Heleper()
# print(c.Addition(10,20))
# print(module1.Maths_Heleper._protectdMethod())
# c._Maths_Heleper__priveatemethod()#using namemagnling 
#print(module1.Maths_Heleper.__priveatemethod())# private method no access


# print(module1.configData.pi)
# print(module1.configData._radius);
# #print(module1.configData.__diamter);# no access bcoz private variable
# module1.configData.show(module1.configData.pi+2.55)

# a=Itrator.my_class()
# a.show() 
# a.ChekItrator()

# a.Method()#genertor
print("End")


