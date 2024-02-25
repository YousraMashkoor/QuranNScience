import { Typography, Container } from "@mui/material";
import { Heading, Image, PageContainer, Text, TextContainer } from "./styles";

const Home = () => {
  return (
    <PageContainer maxWidth={900}>
      <TextContainer>
        <Heading variant="h2" component={"h4"}>
          The Quranic Science
        </Heading>
        <Text style={{ marginLeft: 0 }}>
          <Typography>
            QScience is a pioneering website dedicated to closing the gap
            between modern science and Quran.
          </Typography>
          <Typography>
            Our mission is to identify and analyze various patterns found with
            the Quran, making them easily accessible by the harnessing the power
            of AI, our platform continually expands its knowledge base,
            uncovering new patterns and connections that may have been
            previously overlooked.
          </Typography>
        </Text>
      </TextContainer>
      <Container>
        <Image
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2DuX5nccmOPjXjETTWJyQ7vQipKQu5K6C_Q&usqp=CAU"
          alt="image"
        />
      </Container>
    </PageContainer>
  );
};

export default Home;
