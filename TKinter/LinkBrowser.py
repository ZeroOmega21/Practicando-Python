import tkinter as tk
import webbrowser

def youTube_link(event):
    webbrowser.open("https://www.youtube.com/watch?v=gZU62nDSb1c")
def github_link(evevnt):
    webbrowser.open("https://github.com/ZeroOmega21")

root = tk.Tk()
root.geometry("300x200")
root.title("Link Browser Example")
label = tk.Label(text="Links:")
label.grid(column=0, row=0)

#Imagenes de los enlaces
MaliceMizer = tk.PhotoImage(file="TKinter\img\MaliceMizer_memoire.png")
PhotoGitHub = tk.PhotoImage(file="TKinter\img\PhotoGitHub.jpg")
#MaliceMizer = MaliceMizer.subsample(10)
#PhotoGitHub = PhotoGitHub.subsample(10)
MaliceMizer = tk.Label(root, image=MaliceMizer)
MaliceMizer.grid(column=1, row=1)
PhotoGitHub = tk.Label(root, image=PhotoGitHub)
PhotoGitHub.grid(column=3, row=1)

#botones con enlaces
boton1 = tk.Button(root, text="Malice Mizer", command=youTube_link, bg="Pink", fg="black")
boton1.grid(column=1, row=2)
boton2 = tk.Button(root, text="My GitHub Profile", command=github_link, bg="black", fg="white")
boton2.grid(column=3, row=2)

boton1.bind("<Button-1>", youTube_link)
boton2.bind("<Button-1>", github_link)

#insertar imagen
img = tk.PhotoImage(file="TKinter\img\ZeroImg1.png")
#tamaño de la imagen subsample & zoom
img = img.subsample(10)  #reduce el tamaño de la imagen
ImagenZero = tk.Label(root, image=img)
ImagenZero.grid(column=1, row=3)

root.mainloop()