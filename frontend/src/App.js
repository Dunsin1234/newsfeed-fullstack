import {useEffect,useState} from "react";
function App(){
const[news,setNews]=useState(null);
useEffect(()=>{
fetch("http://localhost:5000/news")
.then(res=>res.json())
.then(data=>setNews(data));
},[]);
return(
<div style={{textAlign:"center",padding:"2rem"}}>
<h1>🗞️ NewsFeed</h1>
{news?
(<>
<p><strong>Source:</strong> {news.source}</p>
<h3>{news.data}</h3>
</>)
:(<p>Loading news...</p>)
}
</div>
);
}
export default App;
