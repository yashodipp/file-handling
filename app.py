

import streamlit as st
from pathlib import Path
import os

st.set_page_config(page_title="File Handling System", layout="centered")

st.title("📁 File & Folder Management System")

# ---------- Helper ----------
def list_items():
    p = Path(".")
    items = list(p.rglob("*"))
    if items:
        for i, v in enumerate(items, start=1):
            st.write(f"{i}. {v}")
    else:
        st.info("No files or folders found.")


# ---------- Menu ----------
option = st.selectbox(
    "Select an operation",
    [
        "Create Folder",
        "List Files & Folders",
        "Update Folder Name",
        "Delete Folder",
        "Create File",
        "Read File",
        "Update File",
        "Delete File"
    ]
)

# ---------- Create Folder ----------
if option == "Create Folder":
    name = st.text_input("Enter folder name")
    if st.button("Create Folder"):
        p = Path(name)
        if not p.exists():
            p.mkdir()
            st.success("Folder created successfully.")
        else:
            st.error("Folder already exists.")

# ---------- List ----------
elif option == "List Files & Folders":
    st.subheader("Files & Folders")
    list_items()

# ---------- Update Folder ----------
elif option == "Update Folder Name":
    old = st.text_input("Enter existing folder name")
    new = st.text_input("Enter new folder name")
    if st.button("Rename Folder"):
        old_p = Path(old)
        new_p = Path(new)
        if old_p.exists() and old_p.is_dir():
            if not new_p.exists():
                old_p.rename(new_p)
                st.success("Folder renamed successfully.")
            else:
                st.error("New folder name already exists.")
        else:
            st.error("Folder does not exist.")

# ---------- Delete Folder ----------
elif option == "Delete Folder":
    name = st.text_input("Enter folder name to delete")
    if st.button("Delete Folder"):
        p = Path(name)
        if p.exists() and p.is_dir():
            try:
                p.rmdir()
                st.success("Folder deleted successfully.")
            except:
                st.error("Folder is not empty.")
        else:
            st.error("Folder does not exist.")

# ---------- Create File ----------
elif option == "Create File":
    name = st.text_input("Enter file name (with extension)")
    content = st.text_area("File content")
    if st.button("Create File"):
        p = Path(name)
        if not p.exists():
            with open(p, "w", encoding="utf-8") as f:
                f.write(content)
            st.success("File created successfully.")
        else:
            st.error("File already exists.")

# ---------- Read File ----------
elif option == "Read File":
    name = st.text_input("Enter file name to read")
    if st.button("Read File"):
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r", encoding="utf-8") as f:
                st.text(f.read())
            st.success("File read successfully.")
        else:
            st.error("File does not exist.")

# ---------- Update File ----------
elif option == "Update File":
    name = st.text_input("Enter file name")
    action = st.radio(
        "Choose action",
        ["Rename File", "Overwrite Content", "Append Content"]
    )

    if action == "Rename File":
        new_name = st.text_input("Enter new file name")

    content = st.text_area("Content (for overwrite / append)")

    if st.button("Update File"):
        p = Path(name)
        if not (p.exists() and p.is_file()):
            st.error("File does not exist.")
        else:
            if action == "Rename File":
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    st.success("File renamed successfully.")
                else:
                    st.error("File name already exists.")

            elif action == "Overwrite Content":
                with open(p, "w", encoding="utf-8") as f:
                    f.write(content)
                st.success("File overwritten successfully.")

            elif action == "Append Content":
                with open(p, "a", encoding="utf-8") as f:
                    f.write("\n" + content)
                st.success("Content appended successfully.")

# ---------- Delete File ----------
elif option == "Delete File":
    name = st.text_input("Enter file name to delete")
    if st.button("Delete File"):
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            st.success("File deleted successfully.")
        else:
            st.error("File does not exist.")
