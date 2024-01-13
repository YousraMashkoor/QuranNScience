import { Container, Typography } from '@mui/material';
import styled from 'styled-components';

const PageContainer = styled(Container)`
    background-color: #060359;
    color: white;
    display: flex !important;
    align-items: center;
    padding: 100px !important;
    text-allign: center;
`
const TextContainer = styled(Container)`
    margin: 20px !important;
    & > nth-child(2) {
        margin-top: 20px !important
    }
`

const Image = styled('img') ({
    marginLeft: 150,
    width: 400
})

const Heading = styled(Typography)`
    font-weight: bold !important;
`

const Text = styled(Typography)`
    & > *{
        font-weight: bold !important;
        margin-top: 20px !important;
        margin-left: 15px !important;
    }
`
const Home = () => {
    return(
        <PageContainer maxWidth={900} >
            <TextContainer >
                <Heading variant='h2' component={'h4'} >
                    The Quranic Science
                </Heading>
                <Text style={{marginLeft:0}}>
                    <Typography>
                    QScience is a pioneering website dedicated to closing the gap between modern science and Quran.
                    </Typography>
                    <Typography>
                        Our mission is to identify and analyze various patterns found with the Quran, making them easily accessible by the harnessing the power of AI, our platform continually expands its knowledge base, uncovering new patterns and connections that may have been previously overlooked.
                    </Typography>
                </Text>
            </TextContainer>
            <Container>
                <Image src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2DuX5nccmOPjXjETTWJyQ7vQipKQu5K6C_Q&usqp=CAU"
                alt='image'/>
            </Container>
        </PageContainer>
    );
}

export default Home;