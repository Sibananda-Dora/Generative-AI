import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def check_stock(data):
    print(f"checking : {data}")
    time.sleep(3)
    print(f"Status: Available")

async def main():
    loop= asyncio.get_running_loop()      #thread specific  ,
    with ProcessPoolExecutor() as pool:
        result= await loop.run_in_executor(pool,check_stock,"sugar")
        print(result)
if __name__=="__main__":
 asyncio.run(main())