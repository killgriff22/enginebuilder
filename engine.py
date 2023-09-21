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
        nofb = int(input("Enter the number of banks\n>>"))
        nofcpb = int(input("Enter the number of cylinders per bank\n>>"))
        cylinders=[] #holds all cylinder numbers
        banks = [] #holds cylinder numbers by bank
        Banks = [] #holds the bank objects 
        offsets = [] #holds degree offsets of cylinders
        for _ in range(nofb):
            banks.append([])
        for i in range(nofcpb):
            for b in range(nofb):
                cylinders.append(i * nofb + b)
                banks[b].append(i * nofb + b)
                print(f"added cylinder {i * nofb + b} to bank {b}")
        for _ in range(nofb):
            offsets.append(int(input(f"please input the offset for bank {_}\n>>")))
        for i,bank in enumerate(banks):
            Banks.append(engine_generator.Bank(bank,offsets[i]))
        engine = engine_generator.Engine(Banks, cylinders)
    items = ['engine_name','stroke','bore','chamber_volume','starter_torque','starter_speed','idle_throttle_plate_position','rod_length','simulation_frequency','redline','rev_limit','intake_flow_rate']
    for i,item in enumerate(items):
        print(f"{i+1}. change {item} ({getattr(engine,item)})")
    inp = input(">>")
    while not inp == "" and not int(inp) == len(items)+1:
        for i,item in enumerate(items):
            print(f"{i+1}. change {item} ({getattr(engine,item)})")
        print(f"{len(items)+1}. generate")
        inp=int(inp)
        if inp == 1:
            engine.engine_name = input("enter engine name\n>>")
        elif inp == 2:
            engine.stroke = float(input("enter stroke\n>>"))
        elif inp == 3:
            engine.bore = float(input("enter bore\n>>"))
        elif inp == 4:
            engine.chamber_volume = float(input("enter chamber volume\n>>"))
        elif inp == 5:
            engine.starter_torque = float(input("enter starter torque\n>>"))
        elif inp == 6:
            engine.starter_speed = float(input("enter starter speed\n>>"))
        elif inp == 7:
            engine.idle_throttle_plate_position = float(input("enter idle throttle plate position\n>>"))
        elif inp == 8:
            engine.rod_length = float(input("enter rod length\n>>"))
        elif inp == 9:
            engine.simulation_frequency = int(input("enter simulation frequency\n>>"))
        elif inp == 10:
            engine.redline = int(input("enter redline\n>>"))
        elif inp == 11:
            engine.rev_limit = int(input("enter rev limit\n>>"))
        elif inp == 12:
            engine.intake_flow_rate = int(input("enter intake flow rate\n>>"))
        inp = input(">>")
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