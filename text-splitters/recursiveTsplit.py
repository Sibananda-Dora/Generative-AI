from langchain_text_splitters import RecursiveCharacterTextSplitter

text='''
(WSL) is a component of Microsoft Windows that allows the use of a Linux environment from within Windows, foregoing the overhead of a virtual machine and being an alternative to dual booting. The WSL command-line interface tool is installed by default in Windows 11, but a distribution must be downloaded and installed through it before use.[3] In Windows 10, WSL can be installed either by joining the Windows Insider program or manually via Microsoft Store or Winget.[4]

The original version, WSL 1, differs significantly from the second major version, WSL 2. WSL 1 (released August 2, 2016), acted as a compatibility layer for running Linux binary executables (in ELF format) by implementing Linux system calls in the Windows kernel.[5] WSL 2 (announced May 2019[6]), introduced a real Linux kernel – a managed virtual machine (via Hyper-V) that implements the full Linux kernel. As a result, WSL 2 is compatible with more Linux binaries as not all system calls were implemented in WSL 1.[7]

Microsoft offers WSL for a variety of reasons. Microsoft envisions WSL as "a tool for developers – especially web developers and those who work on or with open source projects".[8] Microsoft also claims that "WSL requires fewer resources (CPU, memory, and storage) than a full virtual machine" (a common alternative for using Linux in Windows), while also allowing the use of both Windows and Linux tools on the same set of files.'''

splitter=RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
)
chunks=splitter.split_text(text)
print(len(chunks))
print(chunks)