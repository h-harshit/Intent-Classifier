# Intent-Classifier
This classifier tells whether the underlying intention behind a statement is among these:

 'faq.application_process'
 
 'contact.contact'
 
 'faq.borrow_use'
 
 'faq.biz_simpler'
 
 'faq.borrow_limit'
 
 'faq.biz_new'
 
 'faq.apply_register'
 
 'faq.approval_time'
 
 'faq.address_proof'
 
 'faq.banking_option_missing'
 
 'faq.biz_category_missing'
 
 'faq.aadhaar_missing'
 
 'commonQ.bot'
 
 'commonQ.assist'
 
 'commonQ.name'
 
 'faq.bad_service'
 
 'commonQ.how'
 
 'commonQ.not_giving'
 
 'commonQ.query'
 
 'commonQ.wait'
 
 'commonQ.just_details'
 
 The intent classifier was developed for a chat bot to identify the intent behind the statement and then reply accordingly.
 The classifier can also classify the input statements fed in Hindi-English coded SMS Lingo.
 
 The classifier was first trained on dataset in English only. This model was having hard time to deal with statements in SMS Lingo which 
 is quite common in real life scenario. People usually converse in two languages coded together in the form of SMS lingo.
 For example: Instead of asking the bot 'Can you help me?' the usual question asked by native hindi speakers is "kya aap meri help kar 
 skte hai?"
 
 The workaround this problem was to develop a new dataset by translating the dataset in English to Hindi and then coding it in 
 SMS Lingo and then merging it with the existing dataset. But manual translation would have been a very hectic task so I took help
 of google translate which has this feature of giving translated output in SMS lingo and to automate this task I wrote a simple python
 script.
 
Interestingly, this workaround improved the accuracy of the model to 95% and I also performed KFold and Stratified-KFold cross-
validation to crosscheck for the stability of the model and it came out very well with around same accuracy.
 
