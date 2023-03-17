# 👥 Customer_classifier

a project that uses kmeans clustering algorithm to divide customers into 5 groups, so that better financial descions can be made

CHECK DEMO_VIDEO TO SEE THE OUTPUTS AND READ THE HUPYTER NOTEBOOK FOR MORE INFO

# 💡need for the model

the mall in the dataset wants to make better financial descions and offer better deals to their customers. to do this they want to "know" their customers more. this project classfies customers into five groups on the basis of their annual income and spending score
so the mall can give specific offers for specific target group.

# 1) mail_analysis_and_model_selection.ipynb

## 📚 about the dataset 

#### 📙 Mall_Customers.xls

this dataset has the following information of 200 mall customers

| #  | Column                 |  Non-Null Count |  Dtype | 
|:---: | :-----:              |  :--------------: |  :-----: | 
| 0  | CustomerID             |  200 non-null   |  int64 | 
| 1  | Gender                 |  200 non-null   |  objec |t
| 2  | Age                    |  200 non-null   |  int64 | 
| 3  | Annual Income (k$)     |  200 non-null   |  int64 | 
| 4  | Spending Score (1-100) |  200 non-null   |  int64 | 

in our dataset:

| # |  name | description |
|:---: | :------: | :--------------: | 
| 0.  |  CustomerID             |  Unique ID assigned to the customer                                         |                                 
| 1.  |  Gender                 |  Gender of the customer                                                     |     
| 2.  |  Age                    |  Age of the customer                                                        | 
| 3.  |  Annual Income (k$)     |  Annual Income of the customer in thousands                                 |
| 4.  |  Spending Score (1-100) |  Score assigned by the mall based on customer behavior and spending nature  | 



## 🖋️ both the Customer_classifier.pyw and mail_analysis_and_model_selection.ipynb read this to train their models and show output.

# 🛣️ Roadmap of the project

### 🛠️ 1.Preliminary data analysis:
Edit the data to prepare it for further analysis, describe the key features of the data, and summarize the results.

* the program reads the data from Mall_Customers.xls 
* removes the CustomerID  Column

### ⛓️ 2.Exploratory data analysis:

Investigate data sets and summarize their main characteristics, often employing data visualization methods

* heavy Exploratory data analysis has been done on the dataset

* interactive graphs visualizing insights like:

* A) annual income of the customers
![image](https://user-images.githubusercontent.com/91218998/225887263-c25e08d1-c4ec-4aaf-8508-8d49dce89cf6.png)

* B) spending score of the customers
![image](https://user-images.githubusercontent.com/91218998/225887539-f30f55e9-a4ae-4ced-b435-b464709b4d23.png)

* C) spending score of the customers with respect to their Ages
![image](https://user-images.githubusercontent.com/91218998/225887685-cd0482e2-529c-42c2-8d67-3809736cfa7f.png)

40 year olds spend the most money in the mall

* D) annual income of the customers with respect to their Ages

![image](https://user-images.githubusercontent.com/91218998/225910100-a80b3fb7-3606-43a2-aaf4-05bb1e9236b1.png)

* E) ratio of male to female customers

![image](https://user-images.githubusercontent.com/91218998/225895332-18ba4760-5fb6-48c9-bb9a-7951debc14aa.png)

![image](https://user-images.githubusercontent.com/91218998/225909393-bbfef5dd-aba5-4662-9337-4e6c388e5e7f.png)

* F) general cluster graph

![image](https://user-images.githubusercontent.com/91218998/225909627-3b58a58c-4396-4e65-b722-0cd373c3a9dd.png)

* G) age of the customers

![image](https://user-images.githubusercontent.com/91218998/225909806-072603f6-0947-40fa-9fa9-3effa2e85fee.png)

### ✏️ this is just the tip of the iceburg many more insights like annual income of the customers with respect to their Ages are extracted in mail_analysis_and_model_selection.ipynb i highly reccomond you read it and find for yourself.

### ⚒️ 3. Data pre-processing:

The dataset is preprocessed in order to check missing values, noisy data, and other inconsistencies before executing it to the algorithm.

* changes the catagorical Column Gender {"Male":0, "Female":1}
* no null values in the dataset

### 🧰 4. Model development & comparison:

Model comparison involves comparing the performance of different models on a given task to identify which model is most effective.

* i didnt find much need to use many algorithms in this project as kmeans did an amazing job at seprating the customers

* the within cluster sum of squares graph and silhouette score graph with respect to num of clusters are as follows respectively:

![image](https://user-images.githubusercontent.com/91218998/225890074-5bab4180-5044-45e4-a6cd-07ccf13fab21.png)

![image](https://user-images.githubusercontent.com/91218998/225890167-4ccfb1e3-a9ba-430f-993f-b7b5229a9a08.png)

* it is clear that 5 clusters is the sweet spot

* the customer cluster graph is as follows: 

![image](https://user-images.githubusercontent.com/91218998/225890339-44803db8-06d9-4494-af55-912206bc79ea.png)

* 🖌️ to see how the kmeans model was made indepth check the mail_analysis_and_model_selection.ipynb

# ----------------------------------------------------------------

# 2) customer_classifier.pyw

# 🪟 inputs and outputs of customer_classifier.pyw 

### i would reccomond you watch the demo_video attached in the files as it would give you a clear image on what the project looks like but here are some Screenshots of the GUI

### input of 100, 100:-

![image](https://user-images.githubusercontent.com/91218998/225891876-27e107f8-e7ff-47d7-8c9e-e891cf10bd80.png)

### output msgbox:-

* since the custoemr has a high AI and SS they belong to cluster 2 - purple - "rich shopoholic"

![image](https://user-images.githubusercontent.com/91218998/225892121-e65dda3e-69b1-4792-a720-230a0c6a9cd9.png)

### image of customer graph:-

* the cluster where the customer lies is in cayn the top right cluster

![image](https://user-images.githubusercontent.com/91218998/225893383-13a14402-5b78-47a5-aa90-92e70f4a3f09.png)

# Conclusion

after analysing the data and training the model these insights have been extracted

* the avarage income of the customer in our dataset is 65,000 USD which is almost double than an avarage person from US :31,133 USD (2019)

* the age group we are dealing with is grown adult as the avrage age of customers accross the dataset is 38.8 (min: 13, max: 70) 

* i am asumming the higher someones spending score is the more they spend in the mall therefore by this logic, mostly everyone spends almost the same amount of money in the mall as the avarage is 50 with exceptions

* data is a little biased towards females with 56 percent of the cutomers being female and rest 44 male

* The age range of 20-39 is the most common with almost 50 percent of the customers fall into this bin

* the most common range is 60,000 to 80,000 USD with 70 out of 200 cutomers in this range

* we can see that most of the people have a spending score of 40-50 meaning people shop in bulk (monthly groceries) rather than 1-2 small items at a time 

* in our dataset the female customers are earning more money than male customers

* female customers are spending more money in the mall compared to the male customers

* the mall should target people of age range 30-40 (females) wants the most as they are earing more money and spending a lot of it in the mall

* the customers are seprated into 5 clusters:-

* cluster 0 - green - "rich savers" - these customers have an AI of greater than 70k and but an SS of 0-40 (they hoard their money)
* cluster 1 - red - "wise customers" - these customers have an anual income (AI) of 40k - 80k and a spending score (SS) of 35-65 (wise)
* cluster 2 - purple - "rich shopoholics" - these customers have an AI of greater than 70k and an SS of 60-100 (the ideal customers of the mall)
* cluster 3 - orange - "broke shopoholics" - these customers have an AI of 0-40k but an SS of 60-100 (they are broke but spend a lot money)
* cluster 4 - blue - "broke savers" - these customers have an AI of 0-40k and SS of 0-40 (they dont earn as much and are not intrested)

 	🖍️ many more insights have been done in the mail_analysis_and_model_selection.ipynb

# ⛔ Limitations

* the project is available onlyon pc with python installed

# 🔜 future upgrades for the project

* The model can have its own dedicated website and mobile app
* extracting more insights from the dataset

# 👨‍🦱 credits and contact info

* made by Aryan Rathore
* LinkedIn : https://www.linkedin.com/in/aryan-rathore-b15459215/
* email: aryanrathore13572002@gmail.com, aryan.rathore2021@vitbhopal.ac.in

# ----------------------------------------------------------------
