from lightning_sdk import Studio, Machine

# Create or connect to a studio
s = Studio("my-gpu-job")
s.start()

# Switch to a specific GPU machine
s.switch_machine(Machine.T4)  # or Machine.L4, Machine.A100, Machine.H100

# Run your Python script on the GPU
s.run("python train.py")

# Stop the machine when done to save credits
s.stop()