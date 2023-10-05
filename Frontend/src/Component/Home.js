import './Home.css';
import bg from '../assets/bg.jpg'
import { NavLink } from 'react-router-dom';

function Home() {
  return (
    <div className=''>
      <div>
        <img src={bg} alt='bg' className='w-screen h-screen absolute' />
        <div className='absolute font-bold text-white flex items-center space-x-[64rem] '>
          {/* <span className=' mt-[10px] regular text-[2rem]'>By</span> */}
          <span className=' regular text-[4rem] ml-10 '>Technocrats</span>

          <div className=''>
            <NavLink to='/login'><button className='absolute bg-rose-600  w-[140px] h-[40px] text-white font-bold rounded'>Get Started
            </button></NavLink>
            <NavLink to='/login'><button className='absolute bg-rose-600 ml-[10rem] w-[140px] h-[40px] text-white font-bold rounded'>Login
            </button></NavLink>
          </div>
        </div>


        <div className='absolute ml-[38%] mt-[430px]'>
          <h2 className='text-[7rem]'>Phishing</h2>
          {/* <button className='absolute bg-rose-800 mt-[50px] ml-[150px] w-[160px] h-[65px] text-white ring ring-rose-900 rounded text-xl font-bold'>Get Started
        </button> */}
        </div>
      </div>
      <div>

      </div>
    </div>
  );
}

export default Home;
