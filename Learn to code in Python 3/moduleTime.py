import time as tt
current= tt.localtime()
print(current)
print("Transaction completed at: "+ str(current.tm_hour)+ ' h  '+ str(current.tm_min)+ ' min')
tt.time()

# .time() is used to reference the apoc(beginning of time)
# python uses th eunix apoc thus January 1 1970 0h 0min 0sec

# 86400sec = 1day
deliveryTime= tt.time() + (86400 * 7)
print(tt.localtime(deliveryTime))

# Delay next execution
tt.sleep(5)

