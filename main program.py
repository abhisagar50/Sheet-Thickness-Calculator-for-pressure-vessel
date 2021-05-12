from Tkinter import*
import random
import math
root=Tk()
'''
WP-Working Pressure, WT-Working Temperature, fvalue-Stress in N/meter2(text variable),
den: liquid density
tvar: toggel paramreter fot inner and outer/ inner diameter
LH:Liqiud height, J: Weld join Efficincy
ST: Standard thickness, D: Diameter of vessel, CA: Corrosion Allowence
ST, STH :Standard thickness
'''
#Global Varible declaration
WP=DoubleVar()
WT=DoubleVar()
fvalue=DoubleVar()
den=0.0
tvar=IntVar()
LH=0
J=0
ST=0
STH=0
pd=0
D=DoubleVar()
CA=DoubleVar()
LHchk=IntVar()
tvar1=IntVar()
CFH=0
alpha=0
CTH=0
l11=Label(root,font=('Chiller',20,'normal'))
l22=Label(root,font=('Georgia',20,'normal'))
l11.grid(row=11,column=0,sticky='W')
l22.grid(row=13,column=0,sticky='W')
f=0
val=0
#---
root.title('                                                                                                                                                                                          REACTOR DESIGN')
Name1=Label(root,text='Working Pressure' ,bd=0,fg='black',font=('Arial Black',20,'normal')) # root cpontainer For Single page application
def FH(): #Flat head 
    global STH 
    def submit1(): #eventhandler for b1 button
        global STH
        if len(lb1.curselection())==0 and tvar.get()==0:
            St=cfh.get()*((D.get()-2*ST)*(math.sqrt((pd/f))))
        elif len(lb1.curselection())==0 and tvar.get()==1:
            St=cfh.get()*((D.get())*(math.sqrt((pd/f))))
        elif tvar.get()==0:
            
            St=float(lb1.get(lb1.curselection()[0])[-4:-1]+lb1.get(lb1.curselection()[0])[-1])*(D.get()-2*ST)*(math.sqrt((pd/f)))
        else:
            St=float(lb1.get(lb1.curselection()[0])[-4:-1]+lb1.get(lb1.curselection()[0])[-1])*(D.get())*(math.sqrt((pd/f)))
        l11['text']='Thickness of flat head -'+str(St*1000)+'mm\nStandard Available-'+str(STT(St*1000+CA.get()))
        STH=St
        top1.destroy()
    top1=Toplevel()
    cfh=DoubleVar()  #corosion allowence value
    Label2=Label(top1,text='Assuming De=Di')
    Lable1=Label(top1,text='C value for thickness of head manually input-')

    lb1=Listbox(top1,width=50)
    lb1.insert(1,'Flanged flat heads butt welded to shell De=Di; C=0.45')
    lb1.insert(2,'Plates welded to the end of the shell De=Di ; C=0.7')
    lb1.insert(3,'Plates Welded to the end of the shell with additional fillet weld on the inside De=Di; C=0.55')
    
    Entry1=Entry(top1,textvariable=cfh,width=5)
    b1=Button(top1,text='Submit',command=submit1)
    
    Label2.pack()
    lb1.pack()
    Lable1.pack(side=LEFT)
    Entry1.pack(side=LEFT)
    b1.pack(side=LEFT)
def CH(): # Conical Head
    top2=Toplevel()
    cch=DoubleVar()
    z=DoubleVar()
    L1=Label(top2,text='Apex angle in degree-',font=('Calibri',10,'normal'))
    E1=Entry(top2,textvariable=cch,width=20)
    L3=Label(top2,text='Z value-',font=('Calibri',10,'normal'))
    E2=Entry(top2,textvariable=z,width=5)
    L1.grid(row=2,column=0,sticky='W')
    E1.grid(row=2,column=1,sticky='W')
    L3.grid(row=3,column=0,sticky='W')
    E2.grid(row=3,column=1,sticky='W')
    L2=Label(top2,text='Assuming Dk=Di Further calculations will not include corosion allownce')
    L2.grid(row=1,column=0,sticky='W')
    def submit2():
        Z=z.get()
        if tvar.get()==0 :
            Di=D.get()-2*ST
            t1=(pd*Di*Z)/(2*f*J)
            Dk=Di-2*math.sin(math.radians(cch.get()/2))*((1.0/2.0)*math.sqrt((D.get()*t1/math.cos(math.radians(cch.get()/2)))))
            t2=((pd*Dk/(2*f*J-pd)))*(1/math.cos(math.radians(cch.get()/2)))
        elif tvar.get()==1:
            Do=D.get()+2*ST
            t1=(pd*D.get()*Z)/(2*f*J)
            Dk=D.get()-2*math.sin(math.radians(cch.get()/2))*((1.0/2.0)*math.sqrt((Do*t1/math.cos(math.radians(cch.get()/2)))))
            t2=((pd*Dk/(2*f*J-pd)))*(1/math.cos(math.radians(cch.get()/2)))
        l11['text']='Thickness of conical head \n Near the junction including corrosion allowance-'+str(t1*1000+CA.get())+'mm Standard Available-'+str((STT(t1*1000+CA.get())))+'mm \nAway from junction including corrosion allowance-'+str(t2*1000+CA.get())+'mm Standard available-'+str((STT(t2*1000+CA.get())))

        top2.destroy()                                           
    B1=Button(top2,text='Submit',command=submit2)
    B1.grid(row=2,column=2)
def TH(): # Torispherical Head
    global val,t,STH
    top3=Toplevel()
    t=ST
    t1=0
    val=0
    if tvar.get()==0:
        Do=D.get()
    else:
        Do=D.get()+2*ST
    Ri=DoubleVar()
    ri=DoubleVar()
    Sf=DoubleVar()
    C=DoubleVar()
    L1=Label(top3,text='Ri=',font=('Calibri',10,'normal'))
    L2=Label(top3,text='Do',font=('Calibri',10,'normal'))
    L3=Label(top3,text='ri=',font=('Calibri',10,'normal'))
    L4=Label(top3,text='Do',font=('Calibri',10,'normal'))
    L5=Label(top3,text='Sf',font=('Calibri',10,'normal'))
    L6=Label(top3,text='Enter C ',font=('Calibri',10,'normal'))
    L7=Label(top3,text='m',font=('Calibri',10,'normal'))
    E1=Entry(top3,width=5,textvariable=Ri)
    E2=Entry(top3,width=5,textvariable=ri)
    E3=Entry(top3,width=5,textvariable=Sf)
    E4=Entry(top3,width=5,textvariable=C)
    val=0
    def submit3():
        global val,t,STH
        Ro=Ri.get()*Do+t
        ro=ri.get()*Do+t
       
        if val<1:
            val+=1
            
            he=min((math.pow(Do,2)/(4*(Ro))),(math.sqrt(Do*(ro)/2)),(Ro-math.sqrt(((Ro-Do/2)*(Ro+Do/2-2*ro)))))
            L6['text']='Enter C for he/Do='+str(he/Do)+' t/Do='+str(t/Do)
            L6.grid(row=4,column=0)
            E4.grid(row=4,column=1)
            b1['text']='Submit Again'
        else:
            
            t1=pd*Do*C.get()/(2*f*J)
            
            Ro=Ri.get()*Do+t1
            ro=ri.get()*Do+t1
            if (t1-t)>0.001:
                t=t1
                he=min((math.pow(Do,2)/(4*(Ri.get()*Do+t))),(math.sqrt(Do*(ri.get()*Do+t)/2)),(Ro-math.sqrt(((Ro-Do/2)*(Ro+Do/2-2*ro)))))
                L6['text']='Enter C for he/Do='+str(he/Do)+' t/Do='+str(t/Do)
            else:
                if t1<=0.025:
                    Bd=Do+Do/42+2/3*(ri.get()*Do)+2*Sf.get()
                else:
                    Bd=Do+Do/42+2/3*(ri.get()*Do)+2*Sf.get()+t1
                l11['text']='Required Thickness for torispherical head including corrorsion allowance-'+str(t1*1000+CA.get())+'mm\nStandard Available-'+str(STT(t1*1000+CA.get()))+'mm\nConsidering 6% for bending Standard Available-'+str(STT(t1*0.06*1000+t1*1000+CA.get()))+'mm\nBlank Diameter-'+str(Bd)+'m'
                STH=t1
                top3.destroy()
        
    b1=Button(top3,text='Submit',command=submit3)
    L1.grid(row=1,column=0)
    E1.grid(row=1,column=1)
    L2.grid(row=1,column=2,sticky='W')
    L3.grid(row=2,column=0)
    E2.grid(row=2,column=1)
    L4.grid(row=2,column=2,sticky='W')
    L5.grid(row=3,column=0)
    E3.grid(row=3,column=1)
    L7.grid(row=3,column=2,sticky='W')
    b1.grid(row=4,column=2)

    
def STT(LL): #Standard thickness available
    
    SL=[5,5.5,6,7,8,9,10,11,12,14,16,18,20,22,25,28,32,36,40,45,50,56,63,71,80]
    for i in range(0,len(SL)):
        if LL<SL[i]:
            return SL[i]

def sel1(): # Liquid details if container containes liquid other than water
    
    global top,LHchk,LH,den
    den1=DoubleVar()
    LH1=IntVar()
    if int(LHchk.get())==1:
        global top,LH
        def sel4(): #Creating new container to get liquid details
              LH=LH1.get()
              den=den1.get()
              top.destroy()
        
        top=Toplevel()
        l1=Label(top,text='Liquid height in meter-')
        l1.grid(row=1,column=0)
        E1=Entry(top,textvariable=LH1)
        E1.grid(row=1,column=1)
        l2=Label(top,text='Liquid density in  kg/m3-')
        l2.grid(row=2,column=0)
        E2=Entry(top,textvariable=den1)
        E2.grid(row=2,column=1)
        b1=Button(top,command=sel4,text='Submit')
        b1.grid(row=3,column=0)
        LH=int(LH1.get())
        top.mainloop()
                 
        
        
    else:
        LH=0
        return
def sel2(): #Weld joint efficiency factor calculation
    global J
    j=DoubleVar()
    top=Toplevel()
    l1=Listbox(top,width=100) #Drop Down Menu for weld join efficiency(WJE)
    l1.insert(1,'Class I-1.0')
    l1.insert(2,'Class II with double welded butt joint with full penetrartion-0.85')
    l1.insert(3,'Class II with single welded butt joint with backing strip-0.8')
    l1.insert(4,'Class III with double welded butt joint with full penetration-0.7')
    l1.insert(5,'Class III with single welded butt joint with backing strip-0.65')
    l1.insert(6,'Class III with single welded butt joint with backing strip which may not remainn in lace - 0.6')
    l1.insert(7,'Class III with single welded butt joint without backing strip-0.55')
    l1.insert(8,'Class III single full lap joints for circumferential seams only-0.5')
    l1.pack(side=TOP)
    l2=Label(top,text='Manualy input-') #Input tag for getting custom WJE
    l2.pack(side=LEFT)
    E2=Entry(top,textvariable=j)
    E2.pack(side=LEFT)
    def sel3(): # Setting J i.e. WJE
        global J
        if len(l1.curselection())==0:
            J=j.get()
            top.destroy()
        elif int(l1.curselection()[0])==0   :
            J=l1.curselection()[0]
            top.destroy()
        else :
            if int(l1.curselection()[0])<3:
                J=-((int(l1.curselection()[0])-1)*0.05)+0.85
            else :
                J=-((int(l1.curselection()[0])-3)*0.05)+0.7
            top.destroy()
    b2=Button(top,text='Submit',command=sel3)
    b2.pack(side=BOTTOM)
def Nozzel_Thickness(): # Nozzle Insertion
    if tvar.get()==0:
        Do=D.get()
    else:
        Do=D.get()+2*ST
    top4=Toplevel()
    DOO=DoubleVar()
    IP=DoubleVar()
    OP=DoubleVar()
    tvar2=IntVar()
    L1=Label(top4,text='Diameter of opening-')
    L2=Label(top4,text='m')
    R1=Radiobutton(top4,text='Hole in shell',value=0,variable=tvar2)
    R2=Radiobutton(top4,text='Hole in head',value=1,variable=tvar2)
    L3=Label(top4,text='Inside Protrusion-')
    L4=Label(top4,text='Outside Protrusion-')
    L5=Label(top4,text='m')
    L6=Label(top4,text='m')
    E1=Entry(top4,textvariable=DOO)
    E2=Entry(top4,textvariable=IP)
    E3=Entry(top4,textvariable=OP)
    def submit101():
        if tvar2.get()==0:
            A=(DOO.get()+2*CA.get())*ST
            tr=pd*DOO.get()/(2*f*J-pd)
            tn=STT(tr*1000+CA.get())/1000.0
            tc1=tn-(CA.get()/1000.0)
            tc2=tn-2*(CA.get()/1000.0)
            
            H2=min(IP.get(),(math.sqrt((DOO.get()+2*CA.get())*tc2)))
            H1=min(OP.get(),(math.sqrt((DOO.get()+2*CA.get())*tc1)))
            Ao=2*H1*(tn-tr-CA.get())
            Ai=2*H2*(tn-2*CA.get())
            As=(DOO.get()+2*CA.get())*(STT(ST*1000+CA.get())/1000-ST-CA.get())
            A_=Ai+Ao+As
            if A_<A:
                l22['text']='Ring PAD required \n Nozzel thickness-'+str(tr*1000+CA.get())+'mm\nStandard available-'+str(tn*1000)+'mm'
            else:
                l22['text']='NO Ring PAD required \n Nozzel thickness-'+str(tr*1000+CA.get())+'mm\nStandard available-'+str(tn*1000)+'mm'
            top4.destroy()
        elif tvar2.get()==1:
            if tvar1.get()==1:
                l22['text']='Choose Appropriate  head'
            else:
                STH=STH*1.0
                A=(DOO.get()+2*CA.get())*STH
                tr=pd*DOO.get()/(2*f*J-pd)
                tn=STT(tr*1000+CA.get())/1000.0
                tc1=tn-(CA.get()/1000.0)
                tc2=tn-2*(CA.get()/1000.0)
                
                H2=min(IP.get(),(math.sqrt((DOO.get()+2*CA.get())*tc2)))
                H1=min(OP.get(),(math.sqrt((DOO.get()+2*CA.get())*tc1)))
                Ao=2*H1*(tn-tr-CA.get())
                Ai=2*H2*(tn-2*CA.get())
                As=(DOO.get()+2*CA.get())*(STT(STH*1000+CA.get())/1000-STH-CA.get())
                A_=Ai+Ao+As
                if A_<A:
                    l22['text']='Ring PAD required \n Nozzel thickness-'+str(tr*1000+CA.get())+'mm\nStandard available-'+str(tn*1000)+'mm'
                else:
                    l22['text']='NO Ring PAD required \n Nozzel thickness-'+str(tr*1000+CA.get())+'mm\nStandard available-'+str(tn*1000)+'mm'
                top4.destroy()   
                
                
                  
    b11=Button(top4,text='Submit',command=submit101)
    L1.grid(row=1,column=0,sticky='W')
    E1.grid(row=1,column=1,sticky='W')
    L2.grid(row=1,column=2,sticky='W')
    R1.grid(row=2,column=0,sticky='W')
    R2.grid(row=2,column=1,sticky='W')
    L3.grid(row=3,column=0,sticky='W')
    E2.grid(row=3,column=1,sticky='W')
    L5.grid(row=3,column=2,sticky='W')
    L4.grid(row=4,column=0,sticky='W')
    E3.grid(row=4,column=1,sticky='W')
    L6.grid(row=4,column=2,sticky='W')
    b11.grid(row=4,column=3,sticky='W')
def submit():
    global ST,tvar1,pd,f
    f=fvalue.get()
    value=tvar.get()
    
    
    
    if LH==0:
        pd=1.05*WP.get()
    else :
        if (den*9.81*LH)>0.05*WP.get():
            pd=WP.get()+(den*9.81*LH)
        else :
            pd=1.05*WP.get()
     
    
    if (value==1 and int(list1.curselection()[0])==0):
        ST=((pd*D.get())/(2*f*J-pd))
    elif (value==0 and int(list1.curselection()[0])==0):
        ST=((pd*D.get())/(2*f*J+pd))
    elif (value==1 and int(list1.curselection()[0])==1):
        ST=((pd*D.get())/(4*f*J+pd))
    
    else:
        ST=((pd*D.get())/(4*f*J-pd))
    
    
    ca=CA.get()
    T=STT(ST*1000+ca)
    Name6=Label(root,text='Shell Thickness-'+str(1000*ST)+'mm'+'\nStandard Thickness Available-'+str(T),font=('Algerian',20,'normal'))
    Name6.grid(row=9,column=0)
    rb3=Radiobutton(root,text='Flat Head',variable=tvar1,value=0,font=('Calibri',10,'normal'),padx=10.499999999999999111 ,fg='black',state='normal',command=FH)
    rb4=Radiobutton(root,text='Conical Head',variable=tvar1,value=1,font=('Calibri',10,'normal'),padx=10.499999999999999111 ,fg='black',state='normal',command=CH)
    rb5=Radiobutton(root,text='Torispherical head',variable=tvar1,value=2,font=('Calibri',10,'normal'),padx=10.499999999999999111 ,fg='black',state='normal',command=TH)
    rb3.grid(row=10,column=0,sticky='W')
    rb4.grid(row=10,column=1,sticky='W')
    rb5.grid(row=10,column=2,sticky='W')
    b5=Button(root,text="Proceed for nozzel thickness",command=Nozzel_Thickness)
    b5.grid(row=12,column=0)
    
list1=Listbox(root,width=30,height=2)
list1.insert(1,'Cylinder')
list1.insert(2,'Sphere')
list1.grid(row=8,column=0)
#Grid placer to place widgest acc to x-y coordiantes

Name5=Label(root,text='Diameter in meter',font=('Arial Black',20,'bold'))
Entry4=Entry(root,textvariable=D,width=10)

Name5.grid(row=4,column=0,sticky='W')
Entry4.grid(row=4,column=1,sticky='W')

rb1=Radiobutton(root,text='Outer Diameter',variable=tvar,value=0,font=('Calibri',10,'normal'),padx=10.499999999999999111 ,fg='black',state='normal')
rb2=Radiobutton(root,text='Inner Diameter',variable=tvar,value=1,font=('Calibri',10,'normal'),padx=10.499999999999999111 ,fg='black',state='normal')

rb1.grid(row=5,column=0)
rb2.grid(row=5,column=1)

Entry1=Entry(root,textvariable=WP,width=50)
L1=Label(root,text='pascal' ,bd=0,fg='black',font=('Calibri',20,'normal'))
Name2=Label(root,text='Working Temperature' ,bd=0,fg='black',font=('Arial Black',20,'bold'))

Name2.grid(row=2,column=0,sticky='E')

Entry2=Entry(root,textvariable=WT,width=50)
Entry2.grid(row=2,column=1,sticky='W')

L2=Label(root,text='* Celsius' ,fg='black',bd=0,font=('Calibri',20,'normal'))
Name3=Label(root,text='Stress in N/meter2 -',bd=0,fg='black' ,font=('Arial Black',20,'bold'))
frame1=Label(root ,fg='black')
Name4=Label(root,text='Value')
B1=Button(root,text='Weld joint efficiency factor',command=sel2)
B1.grid(row=8,column=1)
CB1=Checkbutton(root,text='Liquid Height',variable=LHchk,command=sel1,onvalue=1,offvalue=0)
CB1.grid(row=7,column=0,sticky='W')

Name6=Label(root,text='Corrosion Allowance-',font=('Arial Black',10,'bold'),padx=0)
Name7=Label(root,text='mm',font=('Arial Black',10,'bold'),padx=0)
Entry5=Entry(root,textvariable=CA,width=4)

Name6.grid(row=7,column=1,sticky='E')
Name7.grid(row=7,column=3,sticky='W')
Entry5.grid(row=7,column=2,sticky='W')

Submit=Button(root,text='Submit',command=submit)
Submit.grid(row=8,column=2)
Entry3=Entry(root,textvariable=fvalue,width=50)
L1.grid(row=1,column=2)
Entry1.grid(row=1,column=1)
Name1.grid(row=1,column=0,sticky='W')
L2.grid(row=2,column=2,sticky='W')
Name3.grid(row=6,column=0,sticky='W')
Entry3.grid(row=6,column=1,sticky='W')
root.mainloop() # event loop creater

