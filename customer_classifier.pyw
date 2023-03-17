########################################################### CREDITS ##############################################################################################

'''
                                                  WELCOME TO THE customer_classifier

                    THIS PROGRAM CLASSIFIES USER INTO 1 OF THE 5 GROUPS TO HELP BUISSNESSES TAKE SMART DESCISIONS

                                                    MADE BY : ARYAN RATHORE 
                                            COMPUTER SCIENCE ENGINEER AT VIT BHOPAL

                                                        CONTACT INFO
                                                aryanrathore13572002@gmail.com
                                               aryan.rathore2021@vitbhopal.ac.in
                                          github :- https://github.com/aryanrathore1012
                                    LINKEDIN - https://www.linkedin.com/in/aryan-rathore-b15459215/
'''

########################################################### IMPORTS ##############################################################################################

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as tmsg
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.cluster import KMeans

########################################################### FUNCTIONS ###################################################################0#########################

'''                                                             IMPORTANT NOTE                                                              
                                  BEFORE YOU RUN THE PROGRAM MAKE SURE YOU READ AND FOLLOW THE LINES BELOW  
                                                       OTHERWISE THE PROGRAM WONT RUN                                                      '''

# 2

'''              MAKE SURE YOU READ THE "mail_analysis_and_model_selection.ipynb" BEFORE USING THIS AS IT HAS THE INFO ON THE DATA
                                            AND WHY USED RANDOM K-MEANS MODEL FOR MY PREDICTIONS                                         '''

# 3

'''   I HAVE TO SPECIFY A FILE PATH TO read the data from (Mall_Customers.xls, and all the images and icons) FILES IF 
    YOU ARE USING OR COPY PASTING MY CODE MAKE YOU CHANGE THE FILE PATHS I HAVE SPECIFIED WHICH FUNCTIONS NEED A 'FILE PATH CHANGE' 
                                                    SO MAKE SURE YOU CHANGE THEM FIRST '''

# 4

''' 
                  ||||||| JUST CHANGE THE FILE PATHS FROM LINE 70 TO 72 AND YOU CAN RUN THE PROGRAM FOR YOURSELF |||||||                   '''


class customer_Classifier:

    def __init__(self) -> None:
        
        '''

            this function does the following tasks in order:

            1. initializes the path variables
            2. read the Mall_Customers.xls saves it into customer_data and fits the data into k-means model
            3. make a window with 3 frames that ask the user for the customers annual income and spending score
            4. checks if the values are correct, if they are incorrect it shows an error and asks to re-enter info
            5. if correct shows the user the output and the customer graph

        '''

        # ----------------------------------------------------------------------------------------------------------------------------
        # 1. initializes the path variables

        self.icon_path = "F://aryans_code_notes//machine_learning//customer_segmentation//icon.ico"
        self.tile_img_path = "F://aryans_code_notes//machine_learning//customer_segmentation//customer_img.jpg"
        self.dataset_path = "F://aryans_code_notes//machine_learning//customer_segmentation//Mall_Customers.xls"

        # ----------------------------------------------------------------------------------------------------------------------------
        # 2. read the Mall_Customers.xls saves it into customer_data and fits the data into k-means model

        # reading the csv and droping all unnecessary columns
        customer_data = pd.read_csv(self.dataset_path)
        customer_data = customer_data.drop(columns=["CustomerID", "Gender", "Age"])

        customer_data = customer_data.values # gives a 2d list with in the form [[Annual Income (k$) , Spending Score (1-100)]]
        

        # from mail_analysis_and_model_selection.ipynb we already know that the best number of clusters is 5 

        self.k_means_model = KMeans(n_clusters=5, init="k-means++", random_state=0)
        prediction = self.k_means_model.fit_predict(customer_data)

        plt.scatter(customer_data[prediction==0,0], customer_data[prediction==0,1], s=80, c="green", label='0, rich savers')
        plt.scatter(customer_data[prediction==1,0], customer_data[prediction==1,1], s=50, c="red", label='1, wise customers')
        plt.scatter(customer_data[prediction==2,0], customer_data[prediction==2,1], s=50, c="purple", label='2, rich shopoholics')
        plt.scatter(customer_data[prediction==3,0], customer_data[prediction==3,1], s=50, c="orange", label='3, broke shopoholics')
        plt.scatter(customer_data[prediction==4,0], customer_data[prediction==4,1], s=50, c="blue", label='4, broke saver')

        # plotting the centroids
        plt.scatter(self.k_means_model.cluster_centers_[:,0], self.k_means_model.cluster_centers_[:,1], s=100, c="black", label="centroids")

        plt.title('segmented customer groups')
        plt.xlabel('Annual Income of the customer')
        plt.ylabel('Spending Score of the customer')
        plt.legend()
        plt.show()

        # ----------------------------------------------------------------------------------------------------------------------------
        # 3. shows customer segmentation graph to the user

        root = Tk() 
        root.geometry("1000x800")
        root.wm_iconbitmap(self.icon_path)
        root.title("Customer_classifier By Aryan Rathore")
        root.config(bg = "#4d194d")

        top_frame = Frame(root, bg = "#312244")
        top_frame.pack(fill=X)

        form_frame = Frame(root, bg="#4d194d")
        form_frame.pack(side=TOP,fill=BOTH)

        bottom_frame = Frame(root, bg="#4d194d")
        bottom_frame.pack(side=BOTTOM)    

        tile_image = Image.open(self.tile_img_path).resize((400,150), Image.ANTIALIAS)
        tile_image = ImageTk.PhotoImage(tile_image)

        photo_label = Label(top_frame,image=tile_image,borderwidth=10,relief=RIDGE,anchor=CENTER)
        photo_label.image = tile_image
        photo_label.pack(side=TOP,pady=(25,0))

        Label(top_frame,text="welcome to customer_classifier",font=("Cascadia Mono SemiBold", 27, "bold italic"),anchor=CENTER,bg='#1d3461',fg='white',borderwidth=5,relief=RIDGE).pack(side=TOP,pady=(25,0),fill=X)

        Label(top_frame,text=f"Enter the annual income in k$ and spending score\nspending score is Score assigned by the mall \nbased on customer behavior and spending nature",font=("Cascadia Mono SemiBold", 20, "bold italic"),fg='white',bg="#1d3461",anchor=CENTER).pack(side=TOP,pady=(10,25),fill=X)

        income_var = StringVar()
        spending_var = StringVar()

        Label(form_frame,text="income of customer",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#4d194d").grid(row=0,column=0,padx=(200,10),pady=(50,25),sticky=W)
        Entry(form_frame,textvariable=income_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=0,column=1,padx=(25,25),pady=(50,25),sticky=W)

        Label(form_frame,text="spending score (1-100)",font=("Cascadia Mono SemiBold",20, "bold italic "),fg='white',bg="#4d194d").grid(row=1,column=0,padx=(200,10),pady=(15,50),sticky=W)
        Entry(form_frame,textvariable=spending_var,font=("Cascadia Mono SemiBold",15, "bold italic ")).grid(row=1,column=1,padx=(25,25),pady=(15,50),sticky=W)


        # --------------------------------------------------------------------------------------------------------
        # 4. checks if the information sent is valid  if not sends error measage

        def check_title_author(k_means_model, prediction):
            
            if str(income_var.get()).isdigit() == False or str(spending_var.get()).isdigit() == False:
                tmsg.showerror("Invalid information","annual income and spending score can only be an integer and not empty. ")

            else:
                

                # --------------------------------------------------------------------------------------------------------
                # 5. if correct shows the user the output and the customer graph

                input_prediction = k_means_model.predict([[income_var.get(),spending_var.get()]]) 

                if input_prediction == 0:
                    tmsg.showinfo("Classification successfull!", '''The customer belongs to cluster : cluster 0 - green - "rich savers"\ncheck the customergraph to see where the cluster lies.\n\nyou can check the jupyter notebook for more info ''')
                    mpl.style.use(["dark_background"])
                    plt.figure(figsize=(10, 7))
                    list(customer_data).append([income_var.get(), spending_var.get()])
                    plt.scatter(customer_data[prediction==input_prediction[0],0], customer_data[prediction==input_prediction[0],1], s=80, c="cyan", label='your customer')                    
                    plt.scatter(customer_data[prediction==1,0], customer_data[prediction==1,1], s=80, c="red", label='1, wise customers')
                    plt.scatter(customer_data[prediction==2,0], customer_data[prediction==2,1], s=80, c="purple", label='2, rich shopoholics')
                    plt.scatter(customer_data[prediction==3,0], customer_data[prediction==3,1], s=80, c="orange", label='3, broke shopoholics')
                    plt.scatter(customer_data[prediction==4,0], customer_data[prediction==4,1], s=50, c="blue", label='4, brake saver')
                    plt.scatter(self.k_means_model.cluster_centers_[:,0], self.k_means_model.cluster_centers_[:,1], s=100, c="white", label="centroids")
                    plt.xlabel("Annual income of the customer in k$")
                    plt.ylabel("Spending score of the customer (1-100)")
                    plt.title(f''' --- CUSTOMER GRAPH ---\n your customer ({income_var.get()}$, {spending_var.get()}) lies in cluster 0, "rich savers"''')
                    plt.legend()
                    plt.show()

                elif input_prediction == 1:
                    tmsg.showinfo("Classification successfull!", '''The customer belongs to cluster : cluster 1 - red - "wise customers" \ncheck the customergraph to see where the cluster lies.\n\nyou can check the jupyter notebook for more info ''')
                    mpl.style.use(["dark_background"])
                    plt.figure(figsize=(10, 7))
                    list(customer_data).append([income_var.get(), spending_var.get()])
                    plt.scatter(customer_data[prediction==0,0], customer_data[prediction==0,1], s=80, c="green", label='0, rich savers')
                    plt.scatter(customer_data[prediction==input_prediction[0],0], customer_data[prediction==input_prediction[0],1], s=80, c="cyan", label='your customer')                    
                    plt.scatter(customer_data[prediction==2,0], customer_data[prediction==2,1], s=80, c="purple", label='2, rich shopoholics')
                    plt.scatter(customer_data[prediction==3,0], customer_data[prediction==3,1], s=80, c="orange", label='3, broke shopoholics')
                    plt.scatter(customer_data[prediction==4,0], customer_data[prediction==4,1], s=50, c="blue", label='4, brake saver')
                    plt.scatter(self.k_means_model.cluster_centers_[:,0], self.k_means_model.cluster_centers_[:,1], s=100, c="white", label="centroids")
                    plt.xlabel("Annual income of the customer in k$")
                    plt.ylabel("Spending score of the customer (1-100)")
                    plt.title(f''' --- CUSTOMER GRAPH ---\n your customer ({income_var.get()}$, {spending_var.get()}) lies in cluster 1, "wise customers"''')
                    plt.legend()
                    plt.show()

                elif input_prediction == 2:
                    tmsg.showinfo("Classification successfull!", '''The customer belongs to cluster : cluster 2 - purple - "rich shopoholics"\ncheck the customergraph to see where the cluster lies.\n\nyou can check the jupyter notebook for more info ''')
                    mpl.style.use(["dark_background"])
                    plt.figure(figsize=(10, 7))
                    list(customer_data).append([income_var.get(), spending_var.get()])
                    plt.scatter(customer_data[prediction==0,0], customer_data[prediction==0,1], s=80, c="green", label='0, rich savers')
                    plt.scatter(customer_data[prediction==1,0], customer_data[prediction==1,1], s=80, c="red", label='1, wise customers')
                    plt.scatter(customer_data[prediction==input_prediction[0],0], customer_data[prediction==input_prediction[0],1], s=80, c="cyan", label='your customer')
                    plt.scatter(customer_data[prediction==3,0], customer_data[prediction==3,1], s=80, c="orange", label='3, broke shopoholics')
                    plt.scatter(customer_data[prediction==4,0], customer_data[prediction==4,1], s=50, c="blue", label='4, brake saver')
                    plt.scatter(self.k_means_model.cluster_centers_[:,0], self.k_means_model.cluster_centers_[:,1], s=100, c="white", label="centroids")
                    plt.xlabel("Annual income of the customer in k$")
                    plt.ylabel("Spending score of the customer (1-100)")
                    plt.title(f''' --- CUSTOMER GRAPH ---\n your customer ({income_var.get()}$, {spending_var.get()}) lies in cluster 2, "rich shopoholics"''')
                    plt.legend()
                    plt.show()

                elif input_prediction == 3:
                    tmsg.showinfo("Classification successfull!", '''The customer belongs to cluster : cluster 3 - orange - "broke shopoholics""\ncheck the customergraph to see where the cluster lies.\n\nyou can check the jupyter notebook for more info ''')
                    mpl.style.use(["dark_background"])
                    plt.figure(figsize=(10, 7))
                    list(customer_data).append([income_var.get(), spending_var.get()])
                    plt.scatter(customer_data[prediction==0,0], customer_data[prediction==0,1], s=80, c="green", label='0, rich savers')
                    plt.scatter(customer_data[prediction==1,0], customer_data[prediction==1,1], s=80, c="red", label='1, wise customers')
                    plt.scatter(customer_data[prediction==2,0], customer_data[prediction==2,1], s=80, c="purple", label='2, rich shopoholics')
                    plt.scatter(customer_data[prediction==input_prediction[0],0], customer_data[prediction==input_prediction[0],1], s=80, c="cyan", label='your customer')
                    plt.scatter(customer_data[prediction==4,0], customer_data[prediction==4,1], s=50, c="blue", label='4, brake saver')
                    plt.scatter(self.k_means_model.cluster_centers_[:,0], self.k_means_model.cluster_centers_[:,1], s=100, c="white", label="centroids")
                    plt.xlabel("Annual income of the customer in k$")
                    plt.ylabel("Spending score of the customer (1-100)")
                    plt.title(f''' --- CUSTOMER GRAPH ---\n your customer ({income_var.get()}$, {spending_var.get()}) lies in cluster 3, "broke shopoholics"''')
                    plt.legend()
                    plt.show()

                elif input_prediction == 4:
                    tmsg.showinfo("Classification successfull!", '''The customer belongs to cluster : cluster 4 - blue - "broke saver"\ncheck the customergraph to see where the cluster lies. ''')
                    mpl.style.use(["dark_background"])
                    plt.figure(figsize=(10, 7))
                    list(customer_data).append([income_var.get(), spending_var.get()])
                    plt.scatter(customer_data[prediction==0,0], customer_data[prediction==0,1], s=80, c="green", label='0, rich savers')
                    plt.scatter(customer_data[prediction==1,0], customer_data[prediction==1,1], s=80, c="red", label='1, wise customers')
                    plt.scatter(customer_data[prediction==2,0], customer_data[prediction==2,1], s=80, c="purple", label='2, rich shopoholics')
                    plt.scatter(customer_data[prediction==3,0], customer_data[prediction==3,1], s=80, c="orange", label='3, broke shopoholics')
                    plt.scatter(customer_data[prediction==input_prediction[0],0], customer_data[prediction==input_prediction[0],1], s=80, c="cyan", label='your customer')

                    plt.scatter(self.k_means_model.cluster_centers_[:,0], self.k_means_model.cluster_centers_[:,1], s=100, c="white", label="centroids")
                    plt.xlabel("Annual income of the customer in k$")
                    plt.ylabel("Spending score of the customer (1-100)")
                    plt.title(f''' --- CUSTOMER GRAPH ---\n your customer ({income_var.get()}$, {spending_var.get()}) lies in cluster 4, "broke saver"''')
                    plt.legend()
                    plt.show()

        Button(bottom_frame, text="submit", bg='#006466', fg='white', borderwidth=5,relief=RAISED,font=("Cascadia Mono SemiBold",15, "bold italic "),command=lambda:check_title_author(self.k_means_model, prediction)).pack(side=BOTTOM,pady=(0,10))
    
        root.mainloop()


s = customer_Classifier()

########################################################### CREDITS ##############################################################################################

'''
                                                  WELCOME TO THE customer_classifier

                    THIS PROGRAM CLASSIFIES USER INTO 1 OF THE 5 GROUPS TO HELP BUISSNESSES TAKE SMART DESCISIONS

                                                    MADE BY : ARYAN RATHORE 
                                            COMPUTER SCIENCE ENGINEER AT VIT BHOPAL

                                                        CONTACT INFO
                                                aryanrathore13572002@gmail.com
                                               aryan.rathore2021@vitbhopal.ac.in
                                          github :- https://github.com/aryanrathore1012
                                    LINKEDIN - https://www.linkedin.com/in/aryan-rathore-b15459215/
'''