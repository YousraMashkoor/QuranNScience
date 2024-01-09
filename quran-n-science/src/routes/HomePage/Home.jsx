import { Container } from '@mui/material';
import styled from 'styled-components';

const PageContainer = styled(Container)`
    background-color: #060359;
    color: white;
    text-allign: center;
`
const Home = () => {
    return(
        <PageContainer maxWidth={900} >
            Hello
        </PageContainer>
    );
}

export default Home;