import sys
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def data_analysis(train_df):

    ### 1: Printing data summary
    print(train_df.info())
    
    ### Plotting the target variable as a histogram
    train_df["Loan_Status"].value_counts(normalize=True).plot(kind='bar')
    plt.savefig('loan_status_plot.png')
    
    
    
    ### Plotting the Categorical Variables 
    plt.figure(1)
    plt.subplot(221)
    train_df["Gender"].value_counts(normalize=True).plot(kind='bar',figsize = (20,10),title='Gender')
    #plt.savefig('gender.png')
 
    plt.subplot(222)
    train_df["Married"].value_counts(normalize=True).plot(kind='bar',title='Married')
    #plt.savefig('married.png')
    
    plt.subplot(223)
    train_df["Self_Employed"].value_counts(normalize=True).plot(kind='bar',title='Self_Employed')
    #plt.savefig('self_employed.png')
    
    plt.subplot(224)
    train_df["Credit_History"].value_counts(normalize=True).plot(kind='bar',title='Credit_History')
    
    plt.savefig('plots_categorical.png')
    
    
    
    
    ### Plotting the Ordinal Variables 
    plt.figure(2)
    plt.subplot(131)
    train_df["Dependents"].value_counts(normalize=True).plot(kind='bar',figsize = (20,10),title='Dependents')
    #plt.savefig('gender.png')
 
    plt.subplot(132)
    train_df["Education"].value_counts(normalize=True).plot(kind='bar',title='Education')
    #plt.savefig('married.png')
    
    plt.subplot(133)
    train_df["Property_Area"].value_counts(normalize=True).plot(kind='bar',title='Property Area')
    #plt.savefig('self_employed.png')
    
  
    
    plt.savefig('plots_ordinals.png')
    
    
    plt.close()
    
   
    
    




if __name__ == "__main__":

    train_df = pd.read_csv('train.csv')
    data_analysis(train_df)