const RED = "rgb(239,83,80)",
      ORANGE = "rgb(255,152,0)",
      YELLOW = "rgb(253,216,53)"

const isInViewport = el => {
  const rect = el.getBoundingClientRect();
  return rect.top >= 0 && rect.bottom <= window.innerHeight
}
const isWayOutOfViewport = el => {
  const rect = el.getBoundingClientRect();
  return rect.top <= -600 || rect.bottom >= (window.innerHeight + 600)
}
const getFizzBuzzProps = i => {
  let text = "",
      textStyle = {},
      borderStyle = {},
      backgroundStyle = {}
  
  if(i % 15 === 0){
    text = `FizzBuzz (${i})`
    textStyle={"color": ORANGE}
    borderStyle={"borderColor": ORANGE}
    backgroundStyle={"backgroundColor": ORANGE}
  }
  else if(i % 3 === 0){
    text = `Fizz (${i})`
    textStyle={"color": RED}
    borderStyle={"borderColor": RED}
    backgroundStyle={"backgroundColor": RED}
  }
  else if(i % 5 === 0){
    text = `Buzz (${i})`
    textStyle={"color": YELLOW}
    borderStyle={"borderColor": YELLOW}
    backgroundStyle={"backgroundColor": YELLOW}
  }
  else{
    text = i.toString();
  }
  
  return {
    text,
    style: {
      text: textStyle,
      border: borderStyle,
      background: backgroundStyle
    }
  }
}

const FizzBuzz = () => {
  const [scrollY, setScrollY] = React.useState(0)
  
  React.useEffect(() => {
    document.addEventListener("scroll", _.throttle(e => setScrollY(window.scrollY), 100))
  }, [])
  
  return(
    <div id="fizz-buzz-app">
      <div id="fizz-buzz-timeline-bar"/>
      <FizzBuzzItems scrollY={scrollY}/>
    </div>
  )
}
  
const FizzBuzzItems = ({scrollY}) => {
  const getFizzBuzzItems = () => {
    let items = []
    for(let i = 1; i <= 100; i++){ items.push(i) }
    return items.map(i => <FizzBuzzItem key={i} i={i} scrollY={scrollY}/>)
  }                 
  return(
    <div id="fizz-buzz-items">
      {getFizzBuzzItems()}
    </div>
  )
}
    
const FizzBuzzItem = ({i, scrollY}) => {
  const itemRef = React.useRef(null)
  
  const [inViewport, setInViewport] = React.useState(false),
        [wayOutOfViewport, setWayOutOfViewport] = React.useState(false)
  
  React.useEffect(() => {
    setInViewport(isInViewport(itemRef.current))
    setWayOutOfViewport(isWayOutOfViewport(itemRef.current))
  }, [scrollY])
  
  const props = getFizzBuzzProps(i)
  
  const getClasses = () => {
    const inViewportClass = inViewport ? "in-viewport" : "not-in-viewport",
          wayOutOfViewportClass = wayOutOfViewport ? "way-out-of-viewport" : ""
    return `item ${props.text.toLowerCase()} ${inViewportClass} ${wayOutOfViewportClass}`
  }
  
  return(
    <div ref={itemRef} style={props.style.border} className={getClasses()}>
      <h1 className="background-text" style={props.style.text}>{props.text}</h1>
      <h1 className="text" style={props.style.text}>{props.text}</h1>
      <div className="bar">
        <div className="dot dot-1" style={props.style.background}/>
        <div className="dot dot-2" style={props.style.background}/>
        <div className="dot dot-3" style={props.style.background}/>
      </div>
      <div className="dot">
        <div className="center" style={props.style.background}/>
        <div className="ring" style={props.style.border}/>
      </div>
    </div>
  )
}
  
  
ReactDOM.render(<FizzBuzz/>, document.getElementById('root'))
