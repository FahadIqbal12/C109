import random
import plotly.figure_factory as ff
import statistics 
#import plotly.express as px
result =[]
count = []
for i in range(0,1000):

    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    result.append(num1+num2)
    count.append(i)
mean = sum(result)/len(result)
median = statistics.median(result)
mode = statistics.mode(result)
std_deviation = statistics.stdev(result)

print("mean of data is : "+ str(mean) )
print("Median is : "+ str(median))
print("mode is : "+ str(mode))
print("Standard Deviation is : "+ str(std_deviation))

first_std_deviaton_start , first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start , second_std_deviation_end = mean - (2* std_deviation), mean + (2*std_deviation)

list_of_data_within_1_std_deviation =[result for result in result if result > first_std_deviaton_start and result < first_std_deviation_end ]
list_of_data_within_2_std_deviation = [result for result in result if result > second_std_deviation_start and result < second_std_deviation_end]

print('{}% of Data lies within first standard deviation'.format(len(list_of_data_within_1_std_deviation)*100.0/len(result)))
print('{}% of Data lies within second standard deviation'.format(len(list_of_data_within_2_std_deviation)*100.0/len(result)))

#fig = px.bar(x=result,y=count)
fig = ff.create_distplot([result],['Result'])
#fig.show()
print(result)



