import "./byeie"; // loučíme se s IE

let host = "https://data.irozhlas.cz"
if (location.hostname === "localhost") {
  host = 'http://localhost'
}

function drawIt(text, comments) {
  let pageLen = 0
    let pageNum = 0
    Object.keys(text).forEach(o => {
      pageLen += text[o].length
      let tmp = `<div id="par_${o}" class="row"><div class="txt">${text[o]}</div>`
      if (o in comments) {
        tmp += `<div class="cmnt" id="cmnt_${o}">${comments[o]}</div>`
      } else {
        tmp += `<div class="cmnt_empty"></div>`
      }
      //cisla stran
      let rw = ''
      if (pageLen >= 3600) {
        pageLen = 0
        pageNum += 1
        rw = `<div class="pagenum">-${pageNum}-</div>`
      }
      document.getElementById("textbx").innerHTML += tmp + `</div>` + rw
    })

    let cst= document.getElementsByClassName('cmnt')
    Array.from(cst, e => e.addEventListener('click', ev => {
      document.getElementById(ev.target.id).classList.add('exp')
    }))
}

let text = null
let comments = null

setTimeout(function() {
  fetch(host + '/ab-sdelovacka/data/text.json')
  .then(response => response.json())
  .then(d => {
    text = d
    if (comments !== null) {
      drawIt(text, comments)
    }
  })

fetch(host + '/ab-sdelovacka/data/comments.json')
  .then(response => response.json())
  .then(d => {
    comments = d
    if (text !== null) {
      drawIt(text, comments)
    }
  })
}, 1)



