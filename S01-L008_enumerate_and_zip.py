projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']


for pos, (project, leader, date) in enumerate(zip(projects, leaders, dates)):
    print(f"{pos+1} - The leader of {project} started {date} is {leader}")
