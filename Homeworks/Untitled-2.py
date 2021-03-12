#!/usr/bin/env python
# coding: utf-8

# In[13]:


Person1={"Name":"Gizem", "Surname": "Deniz", "DateofBirth":"07.02.1991"}
print(Person1)


# In[8]:


print("username :", Person1['Name'])


# In[14]:


print("Name :", Person1['Name'])
print("Surname :", Person1['Surname'])
print("Date of Birth :", Person1['DateofBirth'])


# In[18]:


Person1["email"]="denizgi@itu.edu.tr"
Person1["Adress"]="Lüleburgaz"


# In[19]:


print(Person1)


# In[20]:


print("Name :", Person1['Name'])
print("Surname :", Person1['Surname'])
print("Date of Birth :", Person1['DateofBirth'])
print("Email :", Person1['email'])
print("Adress:", Person1['Adress'])


# In[21]:


Person2={"Name":"Mert", "Surname": "Cömert", "DateofBirth":"04.05.1991", "Email":"mertcomert@su.edu.tr", "Address":"Lüleburgaz"}
print(Person2)


# In[25]:


print("Name :", Person2['Name'])
print("Surname :", Person2['Surname'])
print("Date of Birth :", Person2['DateofBirth'])
print("Email :", Person2['Email'])
print("Address:", Person2['Address'])


# In[26]:


Person3={"Name":"Ahmet", "Surname": "Çetin", "DateofBirth":"01.01.1991", "Email":"ceto@itu.edu.tr", "Address":"Lüleburgaz"}
print(Person3)


# In[27]:


print("Name :", Person3['Name'])
print("Surname :", Person3['Surname'])
print("Date of Birth :", Person3['DateofBirth'])
print("Email :", Person3['Email'])
print("Address:", Person3['Address'])


# In[28]:


Person4={"Name":"Kenan", "Surname": "Tekin", "DateofBirth":"01.01.1991", "Email":"superkeno@itu.edu.tr", "Address":"İstanbul"}
print(Person4)


# In[29]:


print("Name :", Person4['Name'])
print("Surname :", Person4['Surname'])
print("Date of Birth :", Person4['DateofBirth'])
print("Email :", Person4['Email'])
print("Address:", Person4['Address'])


# In[31]:


Person5={"Name":"Seren", "Surname": "Astrosero", "DateofBirth":"01.01.1991", "Email":"astrosero@gmail.edu.tr", "Address":"İstanbul"}
print(Person5)


# In[33]:


Person5["Univercity"]="Istanbul Technical Univercity"
Person5["Master Degree"]="Management Engineering"
Person5["Areas of Interest"]="Astrology"
print(Person5)


# In[34]:


print("Name :", Person5['Name'])
print("Surname :", Person5['Surname'])
print("Date of Birth :", Person5['DateofBirth'])
print("Email :", Person5['Email'])
print("Address:", Person5['Address'])
print("Master Degree:", Person5['Master Degree'])
print("Interest areas:", Person5['Areas of Interest'])


# In[ ]:




