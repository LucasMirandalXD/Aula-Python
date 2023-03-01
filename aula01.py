"""
{
    "liveServer.settings.donotShowInfoMsg": true,
    "explorer.compactFolders": false,
    "code-runner.clearPreviousOutput": true,
    "code-runner.runInTerminal": true,
    "code-runner.executorMap": {
        "python": "cls ; python -u",
    },
    "code-runner.ignoreSelection": true,
    "workbench.colorTheme": "OM Theme (Default Dracula Italic)",
    "workbench.iconTheme": "material-icon-theme",
    "python.defaultInterpreterPath": "python",
}
lembrar de alterar o executorMap de acordo com o sistema operacional
"""
#separador
print (12, "teste", sep='-')
print (12, "teste",12, sep='-')

#escape
print("teste de \"escape\"")

#inverter aspas
print ('tesde de "aspas"')

#type
print( type('teste'))
print( type(True))
#converter tipo
print(int ('1')+2)