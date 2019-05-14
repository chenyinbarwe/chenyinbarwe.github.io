@echo off
xcopy D:\project\blog2\source\_posts D:\project\blog2\source\BACKUP\posts_%date:~0,4%_%date:~5,2%_%date:~8,2%_%time:~0,2%_%time:~3,2%_%time:~6,2% /e/I/d/h/r/y
exit