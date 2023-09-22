import engine_generator
nofcpb = None
nofb = None
cylinders=[] #holds all cylinder numbers
banks = [] #holds cylinder numbers by bank
Banks = [] #holds the bank objects 
offsets = [] #holds degree offsets of cylinders
engine = None
def build():
    global nofcpb, nofb, cylinders, banks, Banks, offsets, engine
    if not engine or input("build new engine?\n>>") in ['y','Y','yes','Yes','YES']:
        nofcb = int()
        cylinders=[] #holds all cylinder numbers
        banks = [] #holds cylinder numbers by bank
        Banks = [] #holds the bank objects 
        offsets = [] #holds degree offsets of cylinders
        radial=False
        if input("Autogenerate radial offsets?\n>>") in ['y','Y','yes','Yes','YES']:
            radial=True
        if input("Autogenerate cyls per bank?\n>>") in ['y','Y','yes','Yes','YES']:
            nofb = int(input("Enter the number of banks\n>>"))
            for _ in range(nofb):#generate the banks
                banks.append([])
            nofcpb = int(input("Enter the number of cylinders per bank\n>>"))
            for i in range(nofcpb):
                for b in range(nofb):
                    cylinders.append(i * nofb + b)
                    banks[b].append(i * nofb + b)
                    print(f"added cylinder {i * nofb + b} to bank {b+1}")
        else:
            nofc = int(input("Enter the number of cylinders\n>>"))
            for i in range(nofc):
                cyln = int(input(f"Enter cylinder {i+1} number (starts at 0)\n>>"))
                cylinders.append(cyln)
                b=int(input(f"Enter the bank number for cylinder {cyln}\n>>"))
                if not b in range(len(banks)):
                    banks.append([])
                banks[b].append(cyln)
            nofb = len(banks)
        if not radial:
            for _ in range(nofb):
                offsets.append(int(input(f"please input the offset for bank {_+1}\n>>")))
        else:
            for _ in range(nofb):
                offsets.append(_ * 360 / nofb)
        for i,bank in enumerate(banks):
            Banks.append(engine_generator.Bank(bank,offsets[i]))
        if input("modify firing order?\n>>") in ['y','Y','yes','Yes','YES']:
            modified_firing_order = []
            for cylinder_number in cylinders:
                new_cylinder_order = int(input(f"Enter firing order for cylinder {cylinder_number} (starts at 1)\n>>"))
                modified_firing_order.append(new_cylinder_order - 1)
            cylinders = modified_firing_order
        engine = engine_generator.Engine(Banks, cylinders)
    items = ['engine_name','stroke','bore','chamber_volume','starter_torque','starter_speed','idle_throttle_plate_position','rod_length','simulation_frequency','redline','rev_limit','intake_flow_rate']
    inp = "0"
    while not inp == "" and not int(inp) == len(items)+1:
        for i,item in enumerate(items):
            print(f"{i+1}. change {item} ({getattr(engine,item)})")
        inp = input(">>")
        if inp == "":
            break
        for i,item in enumerate(items):
            if inp == str(i+1):
                setattr(engine,item,input(f"enter new {item} ({getattr(engine,item)})\n>>"))
                break
    name = input(f"enter engine name {engine.engine_name}\n>>")
    if name:
        engine.engine_name = name
    engine.generate()
    engine.write_to_file(f"{engine.engine_name}.mr")
if __name__ == "__main__":
    while True:
        print(f"""Current Engine: {engine}
{'Build Engine'if engine else 'Build New Engine'}
{'Specs' if engine else 'No Engine'}
{f'Cyl Count: {len(cylinders)}' if engine else ''}
{f'Banks: {len(banks)}' if engine else ''}
{f'Bank Offsets: {offsets}' if engine else ''}
{f'Bank Cylinders: {banks}' if engine else ''}
{f'Engine Name: {engine.engine_name}' if engine else ''}
{f'Stroke: {engine.stroke}' if engine else ''}
{f'Bore: {engine.bore}' if engine else ''}""")
        build()
