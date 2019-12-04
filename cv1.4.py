
# 1.4增加线程方式控制按钮

from tkinter import *
import tkinter.messagebox
import cv2,time,threading

class MainWindow:
    


    def com_r(self,num):
        
        v = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        sz =  (int(v.get(cv2.CAP_PROP_FRAME_WIDTH)),
                int(v.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        fps = 20

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        vout = cv2.VideoWriter()

        video_name = 'V' + time.strftime('%Y%m%d%H%M%S',
            time.localtime(time.time())) + '.mp4'
        vout.open(video_name,fourcc,fps,sz,True)

        cnt = 0
        while cnt < num:

            cnt += 1
            print(cnt)
            ret,frame = v.read()               
            cv2.putText(frame,str(cnt),(2,20),
                cv2.FONT_HERSHEY_PLAIN ,1,(255,255,0), 1, cv2.LINE_AA)
            cv2.putText(frame,'Hello',(2,40),
                cv2.FONT_HERSHEY_PLAIN ,1,(255,255,0), 1, cv2.LINE_AA)
            cv2.imshow('TheFV',frame) 
            vout.write(frame)
            k = cv2.waitKey(1)
            if k == 27:
                break
            elif k == 32:
                cv2.imwrite('P' + time.strftime('%Y%m%d%H%M%S',
                    time.localtime(time.time())) + '.jpg',frame)
           
        
        vout.release()        
        v.release()
        cv2.destroyAllWindows()

    def buttonListener1(self,event): 
        

        th = threading.Thread(target=self.com_r,args=(300,))
        th.setDaemon(True)
        th.start()        

    def buttonListener2(self,event):

        th1 = threading.Thread(target=self.com_r,args=(600,))
        th1.setDaemon(True)
        th1.start()        

    def buttonListener3(self,event):
        tkinter.messagebox.showinfo("messagebox","this is button 3 dialog")
    def buttonListener4(self,event):
        tkinter.messagebox.showinfo("messagebox","this is button 4 dialog")
 
    def  __init__(self):
        self.frame = Tk()
        
        self.button1 = Button(self.frame,text = "15秒录制",width = 10,height = 5)
        self.button2 = Button(self.frame,text = "30秒录制",width = 10,height = 5)
        #self.button3 = Button(self.frame,text = "button3",width = 10,height = 5)
        #self.button4 = Button(self.frame,text = "button4",width = 10,height = 5)
 
        self.button1.grid(row = 0,column = 0,padx = 5,pady = 5)
        self.button2.grid(row = 0,column = 1,padx = 5,pady = 5)
        #self.button3.grid(row = 1,column = 0,padx = 5,pady = 5)
        #self.button4.grid(row = 1,column = 1,padx = 5,pady = 5)
 
        self.button1.bind("<ButtonRelease-1>",self.buttonListener1)
        self.button2.bind("<ButtonRelease-1>",self.buttonListener2)
        #self.button3.bind("<ButtonRelease-1>",self.buttonListener3)
        #self.button4.bind("<ButtonRelease-1>",self.buttonListener4)
 
        self.frame.mainloop()
 
window = MainWindow()
