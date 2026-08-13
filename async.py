import asyncio
import time


async def verify_student():
    print("Verifying student...")
    await asyncio.sleep(2)
    print("Student verified.\n")


async def fetch_attendance():
    print("Fetching attendance...")
    await asyncio.sleep(3)
    print("Attendance loaded.\n")


async def fetch_marks():
    print("Fetching marks...")
    await asyncio.sleep(2)
    print("Marks loaded.\n")


async def main():
    start = time.time()

    # Verify student first
    await verify_student()

    # Run attendance and marks tasks concurrently
    attendance_task = asyncio.create_task(fetch_attendance())
    marks_task = asyncio.create_task(fetch_marks())

    # Wait for both tasks to complete
    await attendance_task
    await marks_task

    end = time.time()
    print(f"\nTotal Time = {end - start:.2f} seconds")


asyncio.run(main())