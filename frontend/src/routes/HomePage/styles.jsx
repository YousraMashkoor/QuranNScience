import { Container, Typography } from "@mui/material";
import styled from "styled-components";

export const PageContainer = styled(Container)`
  background-color: #060359;
  color: white;
  display: flex !important;
  align-items: center;
  padding: 100px !important;
  text-allign: center;
`;

export const TextContainer = styled(Container)`
  margin: 20px !important;
  & > nth-child(2) {
    margin-top: 20px !important;
  }
`;

export const Image = styled("img")({
  marginLeft: 150,
  width: 400,
});

export const Heading = styled(Typography)`
  font-weight: bold !important;
`;

export const Text = styled(Typography)`
  & > * {
    font-weight: bold !important;
    margin-top: 20px !important;
    margin-left: 15px !important;
  }
`;
