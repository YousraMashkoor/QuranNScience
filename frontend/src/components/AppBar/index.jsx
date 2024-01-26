import { useState } from "react";

import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import { Menu, MenuItem } from "@mui/material";

import KeyboardArrowDownIcon from "@mui/icons-material/KeyboardArrowDown";
import ArrowOutwardIcon from "@mui/icons-material/ArrowOutward";
import styled from "styled-components";

const DownArrow = styled(KeyboardArrowDownIcon)`
  margin-left: 0 !important;
`;
const ArrowIcon = styled(ArrowOutwardIcon)`
  margin-left: 0 !important;
  margin-right: 20px;
  padding-left: 0;
`;
export default function ButtonAppBar() {
  const [anchorEl, setAnchorEl] = useState(null);
  const open = anchorEl;

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" style={{ background: "#060359" }}>
        <Toolbar>
          <Typography variant="h4" component="h2" sx={{ flexGrow: 1 }}>
            [Qscience]
          </Typography>
          <Button variant="text" color="inherit">
            Biology
          </Button>
          <Button variant="text" color="inherit">
            Cosmology
          </Button>
          <Button variant="text" color="inherit">
            Physics
          </Button>
          <Button variant="text" color="inherit">
            Archaeology
          </Button>

          <Button variant="text" color="inherit" style={{ paddingRight: 0 }}>
            Climatology
          </Button>
          <DownArrow onClick={handleClick} />
          <Menu
            anchorEl={open}
            keepMounted
            open={open}
            onClose={handleClose}
            anchorOrigin={{
              vertical: "bottom",
              horizontal: "center",
            }}
            transformOrigin={{
              vertical: "top",
              horizontal: "center",
            }}
          >
            <MenuItem onClick={handleClose}>Page to be added</MenuItem>
            <MenuItem onClick={handleClose}>Page to be added</MenuItem>
            <MenuItem onClick={handleClose}>Page to be added</MenuItem>
          </Menu>

          <Button variant="text" color="inherit" style={{ paddingRight: 0 }}>
            Blog
          </Button>
          <ArrowIcon />

          <Button variant="outlined" color="inherit">
            Login
          </Button>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
