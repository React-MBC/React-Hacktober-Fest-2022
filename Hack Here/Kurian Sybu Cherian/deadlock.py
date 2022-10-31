# threads
import threading

# creating locks
lock_state_1 = threading.Lock()
lock_state_2 = threading.Lock()

# using acquire as there are more than one lock


def thread_1():
	while True:
		with acquire(lock_state_1, lock_state_2):
			print('Thread-1')


def thread_2():
	while True:
		with acquire(lock_state_2, lock_state_1):
			print('Thread-2')


t1 = threading.Thread(target=thread_1)

# daemon thread runs without blocking
# the main program from exiting
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()
