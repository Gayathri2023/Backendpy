from email.policy import strict
from sqlmodel import SQLModel, create_engine,Field,Session
from typing import Optional
from sqlalchemy import Column, TIMESTAMP, Integer
from datetime import datetime

DATABASE_URL = "mysql+pymysql://root:nec0914014@localhost:3306/utils"

engine = create_engine(
    DATABASE_URL,
    echo=True
)
print(engine)


#class User(SQLModel, table=True):
#    __tablename__ = "user_list"

#    id: Optional[int] = Field(default=None, primary_key=True)
#    name: str =Field(min_length=3,max_length=20)
#    email: str

class Pdf_template(SQLModel, table=True):
    __tablename__ = "pdf_template"

    pdf_template_id: int = Field(default=None, primary_key=True,description="Unique identifier for the pdf template") 
    pdf_name: str =Field (description="Name of the pdftemplate") 
    pdf_body:str =Field(description="Body for the pdf template") 
    pdf_tem_header:str =Field(description="Header of the pdf")
    pdf_tem_footer:str =Field(description="Footer of the pdf")
    created_date:Optional[datetime] =Field(
    default_factory=datetime.utcnow,
        sa_column=Column(
            TIMESTAMP,
            nullable=False,
            comment="Stores when the record was created"
        )
    )
    modified_date:Optional[datetime] =Field(default_factory=datetime.utcnow,
        sa_column=Column(
            TIMESTAMP,
            nullable=False,comment="Record last updated timestamp"
            ))
    created_by: int =Field(description="Pdf template who created the record")
    modified_by: int =Field(description="Pdf template who last modified")

class Email_template(SQLModel, table=True):
    __tablename__ = "email_template"

    pdf_template_id: int = Field(default=None, primary_key=True,description="unique identifier for the email template") 
    email_temp_name: str =Field (description="Name of the email template") 
    email_temp_subject: str =Field (description="Email subject of the email template") 
    email_temp_body:str =Field(description="Body of the email template") 
    email_temp_header:str =Field(description="Header of the email template")
    email_temp_footer:str =Field(description="Footer of the email template")
    created_date:Optional[datetime] =Field(
    default_factory=datetime.utcnow,
        sa_column=Column(
            TIMESTAMP,
            nullable=False,
            comment="Stores when the record was created"
        )
    )
    modified_date:Optional[datetime] =Field(default_factory=datetime.utcnow,
        sa_column=Column(
            TIMESTAMP,
            nullable=False,comment="Record last updated timestamp"
            ))
    created_by: int =Field(description="Email template who created the record")
    modified_by: int =Field(description="Email template ID who last modified the record")

class Blog_template(SQLModel, table=True):
    __tablename__ = "blog_template"

    blog_id: int = Field(default=None, primary_key=True,description="unique identifier for the blog template") 
    blog_title: str =Field (description="Name of the blog template") 
    blog_body: str =Field (description="blog of the body") 
    blog_author:str =Field(description="Body of the email template") 
    blog_img: str =Field (description="Blog of the image") 
    blog_category:str =Field(description="Category of the body") 
    blog_header:str =Field(description="Header of the blog template")
    blog_footer:str =Field(description="Footer of the blog template")
    created_date:Optional[datetime] =Field(
    default_factory=datetime.utcnow,
        sa_column=Column(
            TIMESTAMP,
            nullable=False,
            comment="Stores when the record was created"
        )
    )
    modified_date:Optional[datetime] =Field(default_factory=datetime.utcnow,
        sa_column=Column(
            TIMESTAMP,
            nullable=False,comment="Record last updated timestamp"
            ))
    created_by: int =Field(description="Blog template who created the record")
    modified_by: int =Field(description="EmailBlog template ID who last modified the record")


SQLModel.metadata.create_all(engine)

#s1=Session(engine)
s2=Session(engine)

#print(s1)
#u1=User(name="ga",email="ezjhkj@google.com")
#s1.add(u1)
#s1.commit()

u2=Pdf_template(pdf_name="InvoiceTemplate",pdf_body="Create an invoice",pdf_tem_header="TemplateCreate",pdf_tem_footer="TemplateCreate@")
u3=Email_template(email_temp_name="InvoiceTemplate",email_temp_subject="create a invoice",email_temp_body="Amazon invoice",email_temp_header="TemplateCreate",email_temp_footer="TemplateCreate@")
u4=Blog_template(blog_title="email blogs",blog_body="blog is email,pdf",blog_author="ravi",blog_img="image ",blog_category="Yes",blog_header="header of the blog",blog_footer="footer of the blog")
s2.add(u2)
s2.commit()
s2.add(u3)
s2.add(u4)
s2.commit()
s2.commit()



#statement = select(User) #.where(User.name == "gayu",User.email=="gay@google.com")
#print("statement",statement)ero = s1.exec(statement).all()
#print(hero)

s2.close()
#s1.close()  