import streamlit as st
st.title("hello geeks for geeks")
st.header("this is header forgeeks")
st.subheader("subheader")
st.text("this is text")
st.markdown("his")
st.markdown("# hi")
st.markdown("## hi")
st.markdown("### hi")
st.markdown("#### hi")

st.success("data is submitted")
st.info("information!")
st.warning("warning!")
st.error("error!")
#display any exception
exp=ZeroDivisionError('division is not possible')
st.exception(exp)
#for getting the documentation
st.help(ZeroDivisionError)

#writting function
st.write("range(1,10)")
st.write(range(1,10))

st.write("1+2+3")
st.write(1+2+3)

st.code('x = 10\n'
        'for i in range(x):\n'
        '\tprint(i)')

st.checkbox('male')
st.checkbox('female')

if(st.checkbox('Adult')):                      #checkbox with validation
    st.write("get a girl and fuck her")


radioButton=st.radio('Select : ',('check','uncheck'))
if(radioButton== 'check'):
    st.write('you are checked')
else:
    st.write(' you are unchecked')   

st.subheader('select Box')
selectbox=st.selectbox("Data science: ",['Datanalysis','ml','ai','web scrapping','nlp'])     
st.write("you have selected",selectbox)

#multiselect box

st.subheader("multi selectbox")
multiselectbox=st.multiselect("Data science: ",['Datanalysis','ml','ai','web scrapping','nlp'])     
st.write("you have selected: ",len(multiselectbox),"courses")

#button

st.subheader("button")
st.button("fuck you")

if(st.button('fuck')):
    st.write("aah")

#slider

st.subheader("slider")
vol=st.slider("select the volume",1.00,10.00,step=0.002)
st.write("the volume is ",vol)

#text input
st.header("text input")
name=st.text_input('name : ')
if(name):
 st.write('hi ',name)

#for username and password
 
st.header("username and password")
name=st.text_input('name: ')
password=st.text_input('password: ')
if(name and password):
   st.write("hello your username is saved")
else:
   st.write("please enter both password and username")   

#text area

st.subheader("text area")
text = st.text_area("write here")
st.write(text)

st.subheader('input number')
st.number_input('select your age',18,110)

st.subheader('input date')
st.date_input('select the date')


st.subheader("input time")
st.time_input('time')


