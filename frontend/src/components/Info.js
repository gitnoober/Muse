import React, { useState, useEffect} from "react";
import { Grid, Button, Typography, IconButton} from "@material-ui/core";
import NavigateBeforeIcon from "@material-ui/icons/NavigateBefore";
import NavigateAfterIcon from "@material-ui/icons/NavigateNext";
import { Link } from "react-router-dom";

const pages = {
    JOIN: 'pages.join',
    CREATE: 'pages.create',

}
export default function Info(props){
    const [page, setPage] = useState(pages.JOIN);

    function joinInfo(){
        return "Join Page"
    }
    function createInfo(){
        return "Create Page"
    }
    useEffect(()=> {
        console.log("ran")
    })
    
    return (
        <Grid container spacing={1}>
            <Grid item xs = {12} align="center">
                <Typography component="h4" variant="h4">
                    What is Muse?
                </Typography>
            </Grid>
            <Grid item xs={12} align="center">
                <Button color="secondary" variant="contained" to="/" component={Link}>
                    Back
                </Button>
            </Grid>
        </Grid>
    )
}
