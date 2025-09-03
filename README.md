# PygamePrompts

This repository contains prompts used for the **ScaDS.AI General Assembly 2025** 2-hour workshop **"Coding Effectively with AI: Getting Started with Cursor and Copilot"**.

## Workshop Overview

**Target Group:** Beginner to intermediate (no coding experience needed)

**Content:** Build a simple Snake game entirely by prompting with Cursor or GitHub Copilot

**Learning Objectives:** Explore different prompting techniques for effective code generation


## Workshop Materials
- [Cursor Download](https://cursor.com/home)
- [Community Pad](https://pad.riseup.net/p/TrS8zBZO1I1feDRa_8ss)

- Slides: TODO

## Linux Cursor Installation 
Please copy the commands one-by-one to your terminal and press Enter. You might need to change the path/file names.

1. Navigate to directory of download file, e.g.: 
```bash
cd Downloads/
```

2. Make file executable:
```bash
 chmod +x Cursor-1.5.9-x86_64.AppImage
```

3. To make Cursor accessible system-wide, move the file to a directory in your PATH, e.g.
```bash
sudo mv Cursor-1.5.9-x86_64.AppImage /opt/cursor/cursor.appimage
```

4. To set up a cursor icon, download the logo for fee from [here](https://lobehub.com/de/icons/cursor) and then move it to the same directory:
 ```bash
sudo mv cursor.png /opt/cursor/
``` 

5. Create a global desktop shortcut (alternative for local shortcut: nano ~/.local/share/applications/cursor.desktop):
```bash
sudo nano usr/share/applications/cursor.desktop
```

6. Add file content & specify icon file path, e.g.:
```bash             
[Desktop Entry]
Name=cursor
Exec=/opt/cursor/cursor.appimage
Icon=/opt/cursor/cursor.png
Type=Application
Categories=Development;
```

In case Cursor doesn't launch try:
```bash             
[Desktop Entry]
Name=cursor
Exec=/opt/cursor/cursor.appimage --no-sandbox
Icon=/opt/cursor/cursor.png
Type=Application
Categories=Development;
```


## Contributors

- Lea Gihlein
- Luisa Götze  
- Mara Lampert
- Lea Kabjesz

## About This Repository

This repository serves as a collection of prompts and examples that demonstrate effective AI-assisted coding techniques. It's designed to help participants learn how to leverage AI tools like Cursor and GitHub Copilot to write code more efficiently, even without prior programming experience.

The prompts contained here showcase various approaches to AI code generation, from basic game mechanics to more complex programming concepts, all focused on creating a complete Snake game through AI assistance.
