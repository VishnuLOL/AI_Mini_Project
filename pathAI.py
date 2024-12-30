from tkinter import *
import backend
from bfs import bi_dir_bfs
from adjancy_matrix_gen import return_matrix

#adjacency_matrix,size=return_matrix()

def gui():
    root = Tk()
    root.title('Traffic Navigation')
    root.geometry('800x780')
    count = 0                                           
    button_list = []                                    

    frame_up = LabelFrame(root, text='options')
    frame_down = LabelFrame(root, text='path')
    frame_up.pack()
    frame_down.pack()
    global supply_mode                                  # for differentiating b/w starting, ending & obstacles point
    supply_mode = 0
    global src                                          # src is starting point
    src = 0
    global block_list                                # stores the obstacles when supply_mode is 2
    block_list = []
    global dest                                         # final destination variable
    dest = 1000
    global traffic_list
    traffic_list =[]

    def button_mode(mode):                              # input field by user starting/obstacles/destination point
        global supply_mode
        supply_mode = mode
        #print(supply_mode)

    def button_click(but_no):                           # clicked buttons in path
        #print(but_no)
        global supply_mode
        if supply_mode == 1:                                # for starting point when supply_mode = 1
            button_list[but_no].config(bg='#ffe525')
            global src
            src = but_no
            start_button['state'] = DISABLED
            supply_mode = 0
        if supply_mode == 2:                                # for obstacles      when supply_mode = 2
            button_list[but_no].config(bg='#696969')
            global block_list
            block_list.append(but_no)
        if supply_mode == 3:                                # for destination    when supply_mode = 3
            button_list[but_no].config(bg='#7dcf21')
            global dest
            dest=but_no
            destination_button['state'] = DISABLED
            supply_mode = 0
        if supply_mode == 4:
            button_list[but_no].config(bg='#d3d3d3')
            global traffic_list
            traffic_list.append(but_no)

    start_button = Button(frame_up, text='Select Start point', command=lambda: button_mode(1))
    block_button = Button(frame_up, text='Select Blocks', command=lambda: button_mode(2))
    destination_button = Button(frame_up, text='Select Destination', command=lambda: button_mode(3))
    traffic_button = Button(frame_up, text='Select Traffic', command=lambda: button_mode(4))


    start_button.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
    block_button.grid(row=0, column=2, sticky="ew", padx=10, pady=5)
    destination_button.grid(row=0, column=3, sticky="ew", padx=10, pady=5)
    traffic_button.grid(row=0, column=4, sticky="ew", padx=10,pady=5)

    for i in range(20):
        for j in range(20):
            button_list.append(Button(frame_down, text=f'{count}', padx=5, pady=5, command=lambda x=count: button_click(x)))
            button_list[count].grid(row=i, column=j, sticky="ew")
            count += 1

    

    def solution():                                         # backend script is called
        parent = backend.backened(src, block_list, traffic_list, dest)
        #parent = bi_dir_bfs(src, dest,adjacency_matrix, 400)
        for value in parent:
            button_list[value].config(bg='#00c5ff')         # path color is turned blue
        button_list[src].config(bg='#ffe525')               # starting pt color is turned back yellow

    go_button = Button(frame_up, text='go', command=solution)
    go_button.grid(row=0, column=5, padx=10, pady=5)

    def restart():
        root.destroy()
        gui()
        
    restart_button = Button(frame_up, text='restart', command=restart)
    restart_button.grid(row=0, column=6, padx=10, pady=5)

    mainloop()
gui()
