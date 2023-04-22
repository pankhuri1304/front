import streamlit as st

st.set_page_config(
    page_title="Olympics Analysis Web App",
    page_icon="https://img.freepik.com/premium-vector/sport-icon-design_24908-6325.jpg",
    layout="wide",
    initial_sidebar_state="expanded",
)


                    #remove top spacing
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

               #Buttom to top button
st.markdown("<div id='LinkToTop'></div>",unsafe_allow_html=True)

# Define the layout of the page

nav_container = st.container()
page_container = st.container()

# Define the content of the navigation container
with nav_container:
    st.write("""
    <style>
        .nav {
            
            text-align:center;
            align-items: center;
            padding: .8rem;
            background: rgb(52,100,255);
            background: linear-gradient(25deg, rgba(52,100,255,1) 0%, rgba(115,233,255,1) 44%, rgba(32,48,255,1) 100%);
        }

        .nav a {
            font-weight:bold;
            font-size: 1.13rem;
            font-family:times new roman;
            margin-right: 1rem;
            margin-left: .5rem;
            color: white;
            text-decoration:none;
            cursor: pointer;
        }

        .nav a:hover {
            background-color: #8cd4ff;
            color: #fff;
            padding:.5rem;
        }

    </style>
    """, unsafe_allow_html=True)

    # Internal Navigation
    st.markdown("<div class='nav'>"
                "<div>"
                                        #Home
                "<a href='#'><img src='https://img.icons8.com/ios-filled/2x/home-page.png' style='width:25px;height:25px; padding-bottom:3px;'> Home</a>"
                
                                 #Summer
                ''' <a target="_self" href="#summer-olympics">
                            <a href="#summer-olympics">
                                <img src='https://img.icons8.com/sf-black-filled/2x/list.png' style='width:25px;height:25px;'> Summer Olympics
                            </a>
                        </a>'''

                                    #Winter
                ''' <a target="_self" href="#winter-olympics">
                            <a href="#winter-olympics">
                            <img src='https://img.icons8.com/glyph-neue/2x/medal2--v1.png' style='width:25px;height:25px;'>Winter Olympics
                            </a>
                        </a>'''
                                    
                                    #Overall
                ''' <a target="_self" href="#overall-analysis">
                            <a href="#overall-analysis">
                            <img src='https://img.icons8.com/ios-filled/2x/geography.png' style='width:23px;height:23px;'>
                                Overall Analysis
                            </a>
                        </a>'''
                
                             #About US
                
                ''' <a target="_self" href="#about-us">
                            <a href="#about-us">
                            <img src = 'https://img.icons8.com/ios-filled/2x/conference-call.png' style = 'width:24px;height:24px;'>
                                About Us
                            </a>
                        </a>'''
                                #Contact
                
                ''' <a target="_self" href="#contact-us">
                            <a href="#contact-us">
                            <img src='https://img.icons8.com/sf-black-filled/2x/new-post.png' style='width:30px;height:30px;'>
                                Contact Us
                            </a>
                        </a>'''
                
                "</div>"

                "</div>"
                "<div id='output'></div>"
                

                ,unsafe_allow_html=True)

                #Flag Image

st.write("")
st.write("")
st.markdown(
    "<center>" '<p> <img src= "https://cdn.pixabay.com/photo/2016/07/22/16/39/olympia-1535219__480.jpg" style="width:100%;height:100%; border: 1px solid #e6e6e6;"> </p>',
    unsafe_allow_html=True)

                #Style and heading
st.markdown("""
            <style>
                .oly-ana {
                    padding-top: 30px;
                    font-size:60px !important;
                    color: #0099e6;
                    text-align:center;
                    font-family: times new roman;
                }
            </style>
            """, unsafe_allow_html=True)
st.markdown('<p class="oly-ana"><b>Olympics Analysis</p>', unsafe_allow_html=True)

st.markdown("""
            <style>
                .detail {
                    font-size:20px !important;
                    color: black;
                    text-align: justify;
                    font-family: times new roman;
                }
            </style>
            """, unsafe_allow_html=True)
st.markdown(
    "<p class='detail'> The modern Olympic Games or Olympics are the leading international sporting events featuring summer and winter sports competitions in which thousands of athletes from around the world participate in a variety of competitions. The Olympic Games are considered the world's foremost sports competition with more than 200 teams, representing sovereign states and territories, participating. </p>",
    unsafe_allow_html=True)
st.markdown(
    "<p class='detail'>Olympism, the spirit of the Olympic Games advocated by Coubertin, is “The elevation of the mind and soul, overcoming differences between nationalities and cultures, embracing friendship, a sense of solidarity, and fair play; ultimately leading to the contribution towards world peace and the betterment of the world. “ This philosophy has been passed down, unchanged, to this day, so Coubertin is considered to be the “Father of the modern Olympics”.</p>",
    unsafe_allow_html=True)

st.markdown("""
            <style>
                .sltctg{
                    font-size:50px !important;
                    color: #0099e6;
                    text-align:center;
                    font-family: times new roman;
                }
            </style>
            """, unsafe_allow_html=True)
st.markdown('<h1 class="sltctg"><b>Select Your Category</b> </h1>', unsafe_allow_html=True)

st.markdown("""
                <style>
                .ssn-name{
                    font-family: times new roman;  
                    color: #ff8000;
                    padding-bottom: 30px;
                    padding-top: 15px;
                }
                </style>
                """, unsafe_allow_html=True)

st.markdown("""
                <style>
                    .ssn-info{
                        width: 100%;
                        font-size:20px !important;
                        color: black;
                        text-align: justify; 
                        font-family: times new roman;    
                }
                </style>
                """, unsafe_allow_html=True)

# summer olympics
st.markdown("# <center><h1 class='ssn-name'>Summer Olympics</h1>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.write(
        "<center>" '<a href="https://isha-agarwal-19-summer-medalsummer-ch6etc.streamlit.app/" target="_blank"> <img src= "https://www.vrfitnessinsider.com/wp-content/uploads/2018/06/anigif_enhanced-buzz-4220-1343595880-0.gif" style="width:100%;height:250px;" > </a>',
        unsafe_allow_html=True)
with col2:
    st.markdown(
        '<p class="ssn-info">The inaugural Games of the modern Olympics were attended by as many as 280 athletes, all male, coming from 12 countries. The athletes competed in 43 events covering athletics (track and field), cycling, swimming, gymnastics, weightlifting, wrestling, fencing, shooting, and tennis. The Summer Olympic Games, also known as the Games of the Olympiad, normally held once every four years. The first Summer Olympic Games, were held in Athens, Greece, 1896. </p>',
        unsafe_allow_html=True)

# winter olympics
st.markdown('# <center><h1 class="ssn-name">Winter Olympics</h1>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.write(
        "<center>" '<a href="https://isha-agarwal-19-winter-medalwinter-spua7v.streamlit.app/", target="_blank"> <img src= "https://i.gifer.com/RSOq.gif" style="width:100%;height:250px;" > </a>',
        unsafe_allow_html=True)
with col2:
    st.markdown(
        '<p class="ssn-info">Although some skating events were included in the 1908 and 1920 Games, it was not until 1924 that the Winter Games were accepted as a celebration comparable to the Summer Games and given the official blessing of the International Olympic Committee (IOC). The Winter Olympic Games is a major international multi-sport event held once every four years for sports practiced on snow and ice. The first Winter Olympic Games, were held in Chamonix, France, 1924.</p>',
        unsafe_allow_html=True)

# overall analysis
st.markdown('# <center><h1 class="ssn-name">Overall Analysis</h1>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.write(
        "<center>" '<a href="https://isha-agarwal-19-overall-medaloverall-ribyis.streamlit.app/", target="_blank"> <img src= "https://themarketingbirds.com/wp-content/uploads/2021/07/1627242520209.gif" style="width:100%;height:250px;" > </a>',
        unsafe_allow_html=True)

with col2:
    st.markdown(
        '<p class="ssn-info">The ideas and work of several people led to the creation of the modern Olympics. The best-known architect of the modern Games was Pierre, baron de Coubertin, born in Paris on New Year’s Day, 1863. At age 24 Coubertin decided that his future lay in education, especially physical education. The Modern Olympic Games are normally held every four years, and since 1994, have alternated between the Summer and Winter Olympics every two years during the four-year period.</p>',
        unsafe_allow_html=True)


# create a container for the footer
footer_container = st.container()

# set the CSS style for the container to make it fixed and position it at the bottom of the page
footer_container.markdown(
    """
    <style>
    
         /* Adjust the font size on smaller screens */
        @media only screen and (max-width: 600px) {
            .footer1 p {
                font-size: 16px;
            }
        }
        /* Adjust the layout on smaller screens */
        @media only screen and (max-width: 600px) {
            .footer1 p {
                display: flex;
                flex-direction: column;
            }
        }
    
    .footer {
        position: float;
        width: 100%;
        background: rgb(32,40,38);
        background: linear-gradient(25deg, rgba(32,40,38,1) 13%, rgba(42,91,91,1) 28%, rgba(73,46,91,1) 51%, rgba(44,75,80,1) 81%, rgba(76,49,78,1) 95%);
        padding: 12px;
        text-align: center;
        font-size: 17px;
        color: black;
        border-top: 1px solid #ddd;
        padding-bottom:.5rem;
    }
    
    .footer p{
        text-align:center;
        padding-top:0px;
        color:#a6a6a6;
        font-family: times new roman;
        font-size: 17px; 

    }
    
    .footer1 a {
        color: #ccffff;
        font-size: 16px;
        
       
    }

    .footer1 h4{
                    font-family: times new roman;  
                    color: white;
                    padding-bottom: 30px;
                    padding-top: 38px;
                }
                
    .footer1{
        position: float;
        width: 100%;
        background: rgb(32,40,38);
        background: linear-gradient(25deg, rgba(32,40,38,1) 13%, rgba(42,91,91,1) 28%, rgba(73,46,91,1) 51%, rgba(44,75,80,1) 81%, rgba(76,49,78,1) 95%);
        padding: 7px;
        text-align: center;
        font-size: 17px;
        color: white;   
    }
    
    .footer1 p{
        text-align:center;
        padding-top:0px;
        margin-left:9rem;
        margin-right: 9rem;
        color:#d9d9d9;
        font-family: times new roman;
        font-size: 17px;  

    }
    
    hr{
    width:0px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# add your footer content to the container
with footer_container:
    st.markdown(
        """ <hr>
            <hr>
        <div class ="footer1"><center>
            <h4> <center> About Us </h4>
            <p>This website is developed by Ms. Pankhuri, Ms. Isha Agarwal, and Mr. Madhav Agarwal as our
            project. We are the students of B.Tech (Computer Science) in Shri Ram Murti Smarak College of Engineering 
            and Technology.</p>
            <p>We would like to thanks our HOD and our project mentor Mr. Hiresh Gupta for the constant support that he
            provided throughout our project journey.</p>
            <h4> <center> Contact Us </h4>
            <div style="display: flex; flex-direction: column;">
                <div style="display: flex;">
                    <div style="flex: 1; color:#d9d9d9;font-family: times new roman;">Isha Agarwal</div>
                    <div style="flex: 1; color:#d9d9d9;font-family: times new roman;">Pankhuri</div>
                    <div style="flex: 1; color:#d9d9d9;font-family: times new roman;">Madhav Agarwal</div>
                </div>
                <div style="display: flex;">
                    <div style="flex: 1;margin-top: 10px;"><a href="mailto:ishaagarwal179@gmail.com">ishaagarwal179@gmail.com</a></div>
                    <div style="flex: 1;margin-top: 10px;"><a href="mailto:pankhurigarg2001@gmail.com">pankhurigarg2001@gmail.com</a></div>
                    <div style="flex: 1;margin-top: 10px"><a href="mailto:madhav.ag56@gmail.com">madhav.ag56@gmail.com</a></div>
                </div>
                <div style="display: flex;">
                    <div style="flex: 1;margin-top: 10px;margin-bottom: 10px"><a href="https://www.linkedin.com/in/isha-agarwal-44120021a/">www.linkedin.com/in/isha-agarwal-44120021a</a></div>
                    <div style="flex: 1;margin-top: 10px"><a href="https://www.linkedin.com/in/pankhuri-613a-/">www.linkedin.com/in/pankhuri-613a-</a></div>
                    <div style="flex: 1;margin-top: 10px"><a href="https://www.linkedin.com/in/madhav-agarwal-b8130b221/">www.linkedin.com/in/madhav-agarwal-b8130b221</a></div>
                </div>
            </div>
        </div>      
        <div class="footer"><center>
            <p><i>© Copyright 2023.</i> </p>
            <p><i>All rights are reserved</i></p>
            <p>• Privacy Policy &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Accessibility &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; • Sitemap  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  • Support</p>   
            <p>© 2023 My Website</p>
            <a target="_blank" title="Follow me on Twitter" href="https://twitter.com/login?lang=en"><img alt="Follow me on Twitter" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Twitter_colored_svg-1024.png" style="width:40px;height:40px;border: 1.5px solid white; border-radius:20%; margin-left:.25rem;padding:2px;"></a>
            <a target="_blank" title="Follow me on Facebook" href="https://www.facebook.com/PLACEHOLDER"><img alt="Follow me on Facebook" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Facebook_colored_svg_copy-1024.png" style="width:40px;height:40px;border: 1.5px solid white; border-radius:20%; margin-left:.25rem;padding:4px;"></a>
            <a target="_blank" title="Send message on WhatsApp" href="https://www.whatsapp.com/"><img alt="Send message on WhatsApp" src=" https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Whatsapp2_colored_svg-1024.png" style="width:40px;height:40px;border: 1.5px solid white; border-radius:20%; margin-left:.25rem;padding:4px;"></a>
            <a target="_blank" title="Follow me on Instagram" href="https://www.instagram.com/"><img alt="Follow me on Instagram" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Instagram_colored_svg_1-1024.png" style="width:40px;height:40px;border: 1.5px solid white; border-radius:20%; margin-left:.25rem;padding:4px;"></a>
            <a target="_blank" title="Follow me on LinkedIn" href="https://in.linkedin.com/"><img alt="Follow me on LinkedIn" src=" https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-1024.png" style="width:40px;height:40px;border: 1.5px solid white; border-radius:20%;margin-left:.25rem;padding:4px;"></a>
            <a target="_blank" title="Send message on Messenger" href="https://www.messenger.com/"><img alt="Send message on Messenger" src="https://cdn4.iconfinder.com/data/icons/social-media-2285/1024/logo-1024.png" style="width:40px;height:40px; border: 1.5px solid white; border-radius:20%; margin-left:.25rem;"></a>   
        </div>
        
        """,
        unsafe_allow_html=True,
    )


                                    #Bottom to top button
st.markdown('''<a href='#LinkToTop'>
            <button id='top'>
                🔝
            </button></a>
            <style>
            #top{
            float: right;
            border: 2px solid black;
            background-color: white;
            margin-top: 80px;
            margin-right: 70px;
            font-size: 30px;
            cursor: pointer;
            border-radius: 20%;
            }
            </style>

            ''', unsafe_allow_html=True)
