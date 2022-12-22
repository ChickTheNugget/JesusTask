from queue import Queue
from random import randint

#temps de calculs 10 min 60 heures
#nouvelle sim toutes les 5 min
#plusieurs coeurs
#10 jours, 24 heures
#le tout sera fait en secondes
#le necessaire 10 * 60 - 6 * 3600
cores_num = 10
days = 10
seconds = 24 * 3600

class Job:
    def __init__(self, start, cores_requested):
        self.time_stamp = start
        self.cores_requested = cores_requested
        self.cpu_time_needed = randint(10 * 60, 6 * 3600)
        self.remaining_time = self.cpu_time_needed / self.cores_requested
    def job_waiting_time(self, time):
        return (time - self.time_stamp)
    def get_time(self):
        return self.time_stamp

class Computer:
    def __init__(self, cores):
        self.cores_total = cores
        self.cores_free = self.cores_total
        self.current_tasks = []
    def start_next_job(self, job):
        self.cores_free -= job.cores_requested
        self.current_tasks.append(job)
    def busy(self, cores):
        return cores.cores_requested > self.cores_free
    def tick(self, second):
        if len(self.current_tasks) > 0:
            for i in range(len(self.current_tasks)):
                i = len(self.current_tasks) - i - 1
                task = self.current_tasks[i]
                task.remaining_time -= 1
                if task.remaining_time <= 0:
                    self.cores_free += task.cores_requested
                    del self.current_tasks[i]


daily_waiting_time = []
daily_total_jobs = []
daily_open_jobs = []
total_waiting_time = 0
total_jobs = 0

def chance(a):
    r = randint(1, a)
    return r == 1

for day in range(days):
    waiting_time = 0
    jobs = 0
    q = Queue()
    c = Computer(cores_num)
    for second in range(seconds):
        if second < 8 * 3600:
            if chance(300):
                q.put(Job(second, randint(1, 10)))
        if not q.empty():
            if not c.busy(q.queue[0]):
                jobs += 1
                new_job = q.get()
                waiting_time += new_job.job_waiting_time(second)
                new_job.time_stamp = second
                c.start_next_job(new_job)
        c.tick(second)
    total_waiting_time += waiting_time
    daily_waiting_time.append(waiting_time)
    daily_total_jobs.append(jobs)
    daily_open_jobs.append(q.qsize())
    total_jobs += jobs

print((total_waiting_time / 60) / total_jobs)
print(total_jobs)
print(daily_waiting_time)
print(daily_total_jobs)
print(daily_open_jobs)



            


    


        