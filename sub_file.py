data = '''id           
job          
work_size    
is_finished  
start_date   
end_date     
team_leader  
collaborators'''
print([i.rstrip() for i in data.split('\n')])