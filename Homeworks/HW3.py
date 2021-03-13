#!/usr/bin/env python
# coding: utf-8

# In[1]:


StudentID1= input("Please enter your Student ID: ")
Midtermgrade1= input("Please enter your Midterm grade: ")
Projectgrade1= input("Please enter your Project grade: ")
Finalgrade1= input("Please enter your Final grade: ")


# In[2]:


StudentID2= input("Please enter your Student ID: ")
Midtermgrade2= input("Please enter your Midterm grade: ")
Projectgrade2= input("Please enter your Project grade: ")
Finalgrade2= input("Please enter your Final grade: ")


# In[3]:


StudentID3= input("Please enter your Student ID: ")
Midtermgrade3= input("Please enter your Midterm grade: ")
Projectgrade3= input("Please enter your Project grade: ")
Finalgrade3= input("Please enter your Final grade: ")


# In[4]:


StudentID4= input("Please enter your Student ID: ")
Midtermgrade4= input("Please enter your Midterm grade: ")
Projectgrade4= input("Please enter your Project grade: ")
Finalgrade4= input("Please enter your Final grade: ")


# In[5]:


StudentID5= input("Please enter your Student ID: ")
Midtermgrade5= input("Please enter your Midterm grade: ")
Projectgrade5= input("Please enter your Project grade: ")
Finalgrade5= input("Please enter your Final grade: ")


# In[6]:


grades={int(StudentID1):(int(Midtermgrade1), int(Projectgrade1), int(Finalgrade1)),int(StudentID2):(int(Midtermgrade2), int(Projectgrade2), int(Finalgrade2)), int(StudentID3):(int(Midtermgrade3), int(Projectgrade3), int(Finalgrade3)), int(StudentID4):(int(Midtermgrade4), int(Projectgrade4), int(Finalgrade4)), int(StudentID5):(int(Midtermgrade5), int(Projectgrade5), int(Finalgrade5))}


# In[7]:


print(grades)


# In[8]:


passinggrade={int(StudentID1):[int(Midtermgrade1)*0.30 + int(Projectgrade1)*0.30 + int(Finalgrade1)*0.40],int(StudentID2):[int(Midtermgrade2)*0.30 + int(Projectgrade2)*0.30 + int(Finalgrade2)*0.40], int(StudentID3):[int(Midtermgrade3)*0.30 + int(Projectgrade3)*0.30 + int(Finalgrade3)*0.40], int(StudentID4):[int(Midtermgrade4)*0.30 + int(Projectgrade4)*0.30 + int(Finalgrade4)*0.40], int(StudentID5):[int(Midtermgrade5)*0.30 + int(Projectgrade5)*0.30 + int(Finalgrade5)*0.40]}


# In[15]:


print(passinggrade)


# In[17]:


liste = list(passinggrade.values())


# In[18]:


print(liste)


# In[20]:


for key, value in passinggrade.items():
    print("{}={}".format(key, value))
    


# In[22]:


yeniliste=sorted(liste)


# In[23]:


print(yeniliste)


# In[ ]:




