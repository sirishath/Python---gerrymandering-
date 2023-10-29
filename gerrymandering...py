"""
Name: Sirisha Thapa
Date: 23rd Oct, 2023
CSC 201
Project 2-Gerrymandering

This programs analyzes the voting in the state entered by the user for a particular election
whose data is stored in a file. The program displays that voting data from that state by district
in a stacked bar chart, displays the statistics by district used to determine gerrymandering,
and computes whether there was gerrymandering in this election in favor of the Democrats or Republicans.

Document Assistance: (who and what  OR  declare that you gave or received no assistance):
I took help from Professor Mueller helped me clear my issue of naming convection and
I also took help from stack exchange,  and previous lab works to find the formula for calculating total window height.



"""

from graphics2 import *

# variables in SCREAMING_SNAKE_CASE remains constant and unchangeable throughout the code 

FILE_NAME = 'districts.txt'
MIN_NUM_DISTRICTS = 2
EFFICIENCY_GAP_LIMIT = 8
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 750
DEFAULT_BAR_HEIGHT = 20
SPACE_BETWEEN = 5

def main():
    
    state_name = input("Which state do you want to look up? ")
    state_name = state_name.title()
    print()
    
    open_file = open(FILE_NAME,'r')
    read_data_in_file = open_file.readlines()
    
    for datas in read_data_in_file:
        if state_name in datas: # this checks if the entered state details is available in the values or folder
            remove_white_space = datas.strip() #removes all the extra white space
            
            convert_list = remove_white_space.split(",")# this converts all the values into list but each value is seperated on the basis of comma
            print(f"District   Democratic Votes   Republican Votes   Surplus Democrat   Surplus Republican")
            surplus_demo_sum = 0
            surplus_rep_sum = 0
            total_demo = 0
            total_rep = 0
            district_list = []
            list_lenght = len(convert_list)
            
            for i in range(1,list_lenght-2,3):
                 district_names = convert_list[i]
                 district_list.append(district_names)
                 
                 demo_votes = int(convert_list[i+1])
                 total_demo = total_demo + demo_votes 
                 
                 rep_votes = int(convert_list[i+2])
                 total_rep = total_rep + rep_votes
                 
                 surplus_demo = 0
                 surplus_rep = 0
                 total_votes_sum = demo_votes + rep_votes

                 
                 if (demo_votes > rep_votes):
                     majority_votes = total_votes_sum // 2 + 1
                     surplus_demo = abs(demo_votes - majority_votes)
                     surplus_demo = int(surplus_demo)
                     surplus_demo_sum = surplus_demo + surplus_demo_sum
                     surplus_rep_sum = rep_votes + surplus_rep_sum
                     surplus_rep = rep_votes
                     
                 elif(rep_votes > demo_votes):
                     majority_vote = total_votes_sum // 2 + 1
                     surplus_rep = abs(rep_votes - majority_vote)
                     surplus_rep = int(surplus_rep)
                     surplus_rep_sum = surplus_rep + surplus_rep_sum
                     surplus_demo_sum = demo_votes + surplus_demo_sum
                     surplus_demo = demo_votes
                 else:
                    surplus_rep_sum = surplus_rep + surplus_rep_sum
                    surplus_demo_sum = demo_votes + surplus_demo_sum
                    surplus_demo = demo_votes
                    surplus_rep = rep_votes
                    
                 print(f'{district_names:>4} {demo_votes:>18,} {rep_votes:>18,} {surplus_demo:>18,} {surplus_rep:>18,} ')
                 
            print()
            
            print(f"Total surplus Democratic votes: {surplus_demo_sum:,}")
            print(f"Total surplus Republican votes: {surplus_rep_sum:,}")
            
            total_votes =  total_demo+total_rep
            num_district = len(district_list)
            
            if (num_district > MIN_NUM_DISTRICTS ) and (surplus_demo_sum > surplus_rep_sum):
                surplus_votes_difference = surplus_demo_sum  - surplus_rep_sum
                efficiency_gap = surplus_votes_difference / total_votes
                efficiency_gap = efficiency_gap * 100
                

                if (efficiency_gap >= EFFICIENCY_GAP_LIMIT):
                    dividing_district = 100 / num_district  
                    gerrymandering_calculation = efficiency_gap / dividing_district
                    print(f"Gerrymandering in {state_name} favoring Republicans worth {gerrymandering_calculation:.2f} congressional seats.")
                    
                else:
                    print(f"No evidence of gerrymandering in {state_name}.")
                    
            elif (num_district > MIN_NUM_DISTRICTS ) and (surplus_demo_sum < surplus_rep_sum):
                surplus_votes_difference = surplus_rep_sum - surplus_demo_sum
                efficiency_gap = surplus_votes_difference / total_votes
                efficiency_gap = efficiency_gap  * 100
            
                if (efficiency_gap >= EFFICIENCY_GAP_LIMIT):
                    dividing_district = 100 / num_district
                    gerrymandering_calculation = efficiency_gap / dividing_district
                    print(f"Gerrymandering in {state_name} favoring Democrats worth {gerrymandering_calculation:.2f} congressional seats.")
                    
                else:
                    print(f"No evidence of gerrymandering in {state_name}.")

    
        
            else:
                print("Gerrymandering computation only valid when more than 2 districts.")
            
      
   # this variables changes each time 
    space_between_change = SPACE_BETWEEN # its first value is 5
    
    # draws/created a window 
    win = GraphWin(f"District Overview for {state_name}", WINDOW_WIDTH, WINDOW_HEIGHT)
    mid_point = WINDOW_WIDTH / 2
    
    # for  drawing a middle dividing line
    
    middle_line = Line(Point(mid_point,0),Point(mid_point,WINDOW_HEIGHT))
    middle_line.draw(win)
    
    # calculating total window height
    
    total_window_height = WINDOW_HEIGHT - 2 * space_between_change - ( num_district - 1) * space_between_change
    max_bar_height =  total_window_height / num_district
    
    # using loop so that all the required datas is received to make a bar graph 
    for i in range(1,list_lenght-2,3):
        district_names = convert_list[i]
        demo_votes = int(convert_list[i+1])
        rep_votes = int(convert_list[i+2])
        total_votes_sum = demo_votes + rep_votes



        # if the maximum height that a bar could take is more than default bar height
        
        if (total_votes_sum > 0) and  max_bar_height >= DEFAULT_BAR_HEIGHT:
            
            bluebar_width = (demo_votes / total_votes_sum) * WINDOW_WIDTH
            redbar_width = WINDOW_WIDTH -  bluebar_width

           
            upperLeft_blue = Point(0,space_between_change)
            lowerRight_blue = Point(WINDOW_WIDTH + bluebar_width, space_between_change + DEFAULT_BAR_HEIGHT)
            blue_bar = Rectangle(upperLeft_blue,lowerRight_blue)
           
            
            lower_right_red = Point(bluebar_width, space_between_change + DEFAULT_BAR_HEIGHT)
            upper_right_red = Point(WINDOW_WIDTH + redbar_width , space_between_change)

            red_bar = Rectangle(lower_right_red,upper_right_red)
            blue_bar.setFill("blue")
            red_bar.setFill("red")
            
            blue_bar.draw(win)
            red_bar.draw(win)
            
            space_between_change = DEFAULT_BAR_HEIGHT + space_between_change + SPACE_BETWEEN
        
        # if the maximum height that a bar could take is less than default bar height
        
        elif (total_votes_sum > 0) and  max_bar_height < DEFAULT_BAR_HEIGHT:
            bluebar_width = (demo_votes / total_votes_sum) * WINDOW_WIDTH
            redbar_width = WINDOW_WIDTH -  bluebar_width

           
            upperLeft_blue = Point(0,space_between_change)
            lowerRight_blue = Point(bluebar_width, space_between_change + max_bar_height)
            blue_bar = Rectangle(upperLeft_blue,lowerRight_blue)
        
            
            lower_right_red = Point(bluebar_width, space_between_change + max_bar_height)
            upper_right_red = Point(redbar_width + WINDOW_WIDTH, space_between_change)

            red_bar = Rectangle(lower_right_red,upper_right_red)
            blue_bar.setFill("blue")
            red_bar.setFill("red")
            
            blue_bar.draw(win)
            red_bar.draw(win)
            
            space_between_change = max_bar_height + space_between_change + SPACE_BETWEEN 
            
        # if sum is 0 but max bar height is less than default bar height    
        elif (total_votes_sum == 0) and  max_bar_height <= DEFAULT_BAR_HEIGHT:
            
             space_between_change = space_between_change + max_bar_height + SPACE_BETWEEN
             
         # if sum is 0 but max bar height is greater than default bar height     
        else:
            space_between_change = space_between_change + DEFAULT_BAR_HEIGHT + SPACE_BETWEEN
            
        



    
            
              
main()
  
  
 