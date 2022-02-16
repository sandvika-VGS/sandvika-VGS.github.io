# Docsify

## Installering

1. Installer node: https://nodejs.org/en/
2. Åpne en terminal, og skriv: npm i docsify-cli -g

## Kjøre lokalt

1. Åpne en terminal i VS Code, og skriv docsify serve .
2. Listening at http://localhost:3000

# Headers

# This is an <h1> tag
## This is an <h2> tag
###### This is an <h6> tag

# Emphasis

*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_

# Lists
## Unordered

* Item 1
* Item 2
  * Item 2a
  * Item 2b

## Ordered

1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b

# Images
![GitHub Logo](/images/logo.png)
![extensions i VS Code](extensions.png ':size=200')

# Links

http://github.com - automatic!
[GitHub](http://github.com)

# Blockquotes
As Kanye West said:

> We're living the future so
> the present is our past.

# Inline code

I think you should use an
`<addr>` element here instead.

# Syntax highlighting
```javascript
function fancyAlert(arg) {
  if(arg) {
    alert(arg)
  }
}
```
```HTML
    <!DOCTYPE html>
    <html>
        <body>
            <h1>Hallo verden!</h1>
        </body>
    </html>
```