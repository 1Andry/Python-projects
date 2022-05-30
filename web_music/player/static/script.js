let butPlay = document.querySelector('.play')
let butPause = document.getElementById('pause')
let butNext = document.querySelector('.next')
let audio = document.querySelector('.audio')
let sounds = document.getElementsByClassName('sound')
let i = 0
butPlay.onclick = function(){
    document.querySelector('audio').play()
    console.log('play')
}
butPause.onclick = function(){
    document.querySelector('audio').pause()
}
butNext.onclick = function(){
    // audio.src = sounds[0+i]
    console.log(sounds[0]+=1)
    // console.log(`i= ${i}`)
}
let songIndex = 0



// console.log(sounds[0])


    

// for (let i=0; i<sounds.length; i++){
//     console.log(sounds[i])
// }


// let player = document.getElementById('current_song')
// console.log(player)



// let audio = document.querySelector('.audio')
// console.log(audio)

// function loadSong(song){
//     audio.src = song
// }
// loadSong(sounds[soundIndex])

// function nextSong (){
//     soundIndex++
// }

// for(let i=0; i<sound.length; i++){
//     console.log(sound[i])
// }