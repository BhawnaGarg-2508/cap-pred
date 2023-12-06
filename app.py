

from flask import Flask,request,render_template
import pickle
from datetime import datetime



app=Flask(__name__)

#loading the model
model=pickle.load(open('Housing_Model','rb'))


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/',methods=['POST'])
def predict():
   #  try:
         '''
        Required input for machine learning model
        1. tradeTime
        2. followers
        3. square
        4. livingRoom
        5. drawingRoom
        6. kitchen
        7. bathRoom
        8. constructionTime
        9. communityAverage
        10. renovationCondition
        11. buildingStructure
        12. elevator
        '''
         #syntax-->  var_name=request.form['<name which in present in html form(index.html)>']
         query_longitude = request.form['Lng']
         query_latitude = request.form['Lat']
         query_tradetime=request.form['tradeTime']
         # query_totalprice = request.form['totalprice']
         # query_followers=request.form['followers']
         query_square=request.form['square']
         query_livingroom=request.form['livingRoom']
         query_drawingroom=request.form['drawingRoom']
         query_kitchen=request.form['kitchen']
         query_bathroom=request.form['bathRoom']
         query_constructiontime=request.form['constructionTime']
         query_communityaverage=request.form['communityAverage']
         query_renovationcondition=request.form['renovationCondition'] #Categorical Data
         query_buildingstructure=request.form['buildingStructure'] #Categorical Data
         query_elevator=request.form['elevator_1.0'] #Categorical Data

         if query_tradetime<query_constructiontime:
             return render_template('index.html')


         #For renovation condition
         # if query_renovationcondition=="renovationCondition_1":
         #    renovationCondition_2=0
         #    renovationCondition_3=0
         #    renovationCondition_4=0
         if query_renovationcondition=="renovationCondition_2":
            renovationCondition_2=1
            renovationCondition_3=0
            renovationCondition_4=0
         elif query_renovationcondition=="renovationCondition_3":
            renovationCondition_2=0
            renovationCondition_3=1
            renovationCondition_4=0
         else:
            renovationCondition_2=0
            renovationCondition_3=0
            renovationCondition_4=1


        # For building structure
         # if query_buildingstructure=="buildingStructure_1":
         #    buildingStructure_2=0
         #    buildingStructure_3=0
         #    buildingStructure_4=0
         #    buildingStructure_5=0
         #    buildingStructure_6=0
         if query_buildingstructure=="buildingStructure_2":
            buildingStructure_2=1
            buildingStructure_3=0
            buildingStructure_4=0
            buildingStructure_5=0
            buildingStructure_6=0
         elif query_buildingstructure=="buildingStructure_3":
            buildingStructure_2=0
            buildingStructure_3=1
            buildingStructure_4=0
            buildingStructure_5=0
            buildingStructure_6=0
         elif query_buildingstructure=="buildingStructure_4":
            buildingStructure_2=0
            buildingStructure_3=0
            buildingStructure_4=1
            buildingStructure_5=0
            buildingStructure_6=0
         elif query_buildingstructure=="buildingStructure_5":
            buildingStructure_2=0
            buildingStructure_3=0
            buildingStructure_4=0
            buildingStructure_5=1
            buildingStructure_6=0
         else:
            buildingStructure_2=0
            buildingStructure_3=0
            buildingStructure_4=0
            buildingStructure_5=0
            buildingStructure_6=1
        
        # For elevator
         if query_elevator=="elevator_1.0":
            elevator_1=0
         else:
            elevator_1=1

         model_data=[[ float(query_longitude),float(query_latitude), float(query_tradetime),float(query_square),float(query_livingroom),
                    float(query_drawingroom),float(query_kitchen),float(query_bathroom),float(query_constructiontime), float(query_communityaverage),
                    int(renovationCondition_2),int(renovationCondition_3),int(renovationCondition_4),
                    int(buildingStructure_2),int(buildingStructure_3),int(buildingStructure_4),int(buildingStructure_5),
                    int(buildingStructure_6),int(elevator_1)]]
        
         print(model_data)
         result=model.predict(model_data)

         print(result)
         
         
         x=float(result)
         y="{:.3f}".format(x)

         return render_template('index.html',results=y)


   #  except ValueError:
   #      return render_template('index.html')
   

if __name__=="__main__":
    app.run(debug=True)






