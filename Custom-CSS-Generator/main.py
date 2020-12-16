# -------------------- All CSS -------------------- #

with open("allcss.css",'w',encoding = 'utf-8') as f:
    f.write("/* -------------------- All CSS -------------------- */\n\n")
    f.write("@import 'margin.css';\n")
    f.write("@import 'paddin.css';\n")
    f.write("@import 'width.css';\n")

# -------------------- Margin -------------------- #

# Margin Around
with open("margin.css",'w',encoding = 'utf-8') as f:
    f.write("/* ---------- Margin Around ---------- */\n\n")
    for i in range(0,101):
        f.write(f".m-{i} {{ margin: {i}px; }}\n")
    else:
        f.write("\n\n")

# Margin Top-Bottom
with open("margin.css",'a',encoding = 'utf-8') as f:
    f.write("/* ---------- Margin Top-Bottom ---------- */\n\n")
    for i in range(0,101):
        f.write(f".my-{i} {{ margin: {i}px 0; }}\n")
    else:
        f.write("\n\n")

# Margin Right-Left
with open("margin.css",'a',encoding = 'utf-8') as f:
    f.write("/* ---------- Margin Right-Left ---------- */\n\n")
    for i in range(0,101):
        f.write(f".mx-{i} {{ margin: 0 {i}px; }}\n")
    else:
        f.write("\n\n")

# Margin Top
with open("margin.css",'a',encoding = 'utf-8') as f:
    f.write("/* ---------- Margin Top ---------- */\n\n")
    for i in range(0,101):
        f.write(f".mt-{i} {{ margin-top: {i}px; }}\n")
    else:
        f.write("\n\n")

# Margin Right
with open("margin.css",'a',encoding = 'utf-8') as f:
    f.write("/* ---------- Margin Right ---------- */\n\n")
    for i in range(0,101):
        f.write(f".mr-{i} {{ margin-right: {i}px; }}\n")
    else:
        f.write("\n\n")

# Margin Bottom
with open("margin.css",'a',encoding = 'utf-8') as f:
    f.write("/* ---------- Margin Bottom ---------- */\n\n")
    for i in range(0,101):
        f.write(f".mb-{i} {{ margin-bottom: {i}px; }}\n")
    else:
        f.write("\n\n")

# Margin Left
with open("margin.css",'a',encoding = 'utf-8') as f:
    f.write("/* ---------- Margin Left---------- */\n\n")
    for i in range(0,101):
        f.write(f".ml-{i} {{ margin-left: {i}px; }}\n")
    else:
        f.write("\n\n")

# -------------------- Padding -------------------- #

# Padding Around
with open("padding.css",'w',encoding = 'utf-8') as f:
    f.write("/* ---------- Padding Around ---------- */\n\n")
    for i in range(0,101):
        f.write(f".m-{i} {{ padding: {i}px; }}\n")
    else:
        f.write("\n\n")

# Padding Top-Bottom
with open("padding.css",'a',encoding = 'utf-8') as f:
    f.write("/* ---------- Padding Top-Bottom ---------- */\n\n")
    for i in range(0,101):
        f.write(f".my-{i} {{ padding-left: {i}px 0; }}\n")
    else:
        f.write("\n\n")

# Padding Right-Left
with open("padding.css",'a',encoding = 'utf-8') as f:
    f.write("/* ---------- Padding Right-Left ---------- */\n\n")
    for i in range(0,101):
        f.write(f".mx-{i} {{ padding: 0 {i}px; }}\n")
    else:
        f.write("\n\n")

# Padding Right
with open("padding.css",'a',encoding = 'utf-8') as f:
    f.write("/* ---------- Padding Right ---------- */\n\n")
    for i in range(0,101):
        f.write(f".mr-{i} {{ padding-right: {i}px; }}\n")
    else:
        f.write("\n\n")

# Padding Left
with open("padding.css",'a',encoding = 'utf-8') as f:
    f.write("/* ---------- Padding Left---------- */\n\n")
    for i in range(0,101):
        f.write(f".ml-{i} {{ padding-left: {i}px; }}\n")
    else:
        f.write("\n\n")


# -------------------- Width -------------------- #

# Width in Percentage
with open("width.css",'w',encoding = 'utf-8') as f:
    f.write("/* ---------- Width ---------- */\n\n")
    for i in range(0,101):
        f.write(f".w-{i} {{ width: {i}%; }}\n")
    else:
        f.write("\n\n")










