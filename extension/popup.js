chrome.tabs.query(
    {
        active: true,
        currentWindow: true
    },
    function(tabs) {

        const url = tabs[0].url;
        const urlobj = new URL(url);
        const videoID =  urlobj.searchParams.get("v");

        fetch(
             `http://127.0.0.1:8000/analyze/${videoId}`
        )
        .then(response => response.json())
        .then(data => {
            document.getElementById("result")
            .innerHTML = `
                <p>😊 Positive: ${data.positive}%</p>
                <p>😐 Neutral: ${data.neutral}%</p>
                <p>😞 Negative: ${data.negative}%</p>`
            ;
        })
    }
);