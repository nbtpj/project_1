from preprocessing import para_clustering
from base_type import Paragrapth
from preprocessing import Preprocessing, LINK_TO_TEMPLATE_FILE


# test tiền xử lí và lưu-load dữ liệu tiền xử lí
# x = Preprocessing()
# print(x.output)

# test phân cụm phân cấp
count = -1
a = Paragrapth(
    "Cystic fibrosis Overview Cystic fibrosis is an inherited disorder that causes severe damage to the lungs, "
    "digestive system and other organs in the body. Cystic fibrosis affects the cells that produce mucus, "
    "sweat and digestive juices. These secreted fluids are normally thin and slippery. But in people with cystic "
    "fibrosis, a defective gene causes the secretions to become sticky and thick. Instead of acting as a lubricant, "
    "the secretions plug up tubes, ducts and passageways, especially in the lungs and pancreas. Although cystic "
    "fibrosis requires daily care, people with the condition are usually able to attend school and work, "
    "and often have a better quality of life than people with cystic fibrosis had in previous decades. Improvements "
    "in screening and treatments mean people with cystic fibrosis now may live into their mid- to late 30s, "
    "on average, and some are living into their 40s and 50s. Cystic fibrosis care at Mayo Clinic Symptoms Screening "
    "of newborns for cystic fibrosis is now performed in every state in the United States. As a result, the condition "
    "can be diagnosed within the first month of life, before symptoms develop. For people born before newborn "
    "screening was performed, it's important to be aware of the signs and symptoms of cystic fibrosis. Cystic "
    "fibrosis signs and symptoms vary, depending on the severity of the disease. Even in the same person, "
    "symptoms may worsen or improve as time passes. Some people may not experience symptoms until adolescence or "
    "adulthood. People with cystic fibrosis have a higher than normal level of salt in their sweat. Parents often can "
    "taste the salt when they kiss their children. Most of the other signs and symptoms of cystic fibrosis affect the "
    "respiratory system and digestive system. However, adults diagnosed with cystic fibrosis are more likely to have "
    "atypical symptoms, such as recurring bouts of inflamed pancreas (pancreatitis), infertility and recurring "
    "pneumonia. The thick and sticky mucus associated with cystic fibrosis clogs the tubes that carry air in and out "
    "of your lungs. This can cause signs and symptoms such as: - A persistent cough that produces thick mucus ("
    "sputum) - Wheezing - Breathlessness - Exercise intolerance - Repeated lung infections - Inflamed nasal passages "
    "or a stuffy nose The thick mucus can also block tubes that carry digestive enzymes from your pancreas to your "
    "small intestine. Without these digestive enzymes, your intestines aren't able to completely absorb the nutrients "
    "in the food you eat. The result is often: - Foul-smelling, greasy stools - Poor weight gain and growth - "
    "Intestinal blockage, particularly in newborns (meconium ileus) - Severe constipation Frequent straining while "
    "passing stool can cause part of the rectum - the end of the large intestine - to protrude outside the anus ("
    "rectal prolapse). When this occurs in children, it may be a sign of cystic fibrosis. Parents should consult a "
    "physician knowledgeable about cystic fibrosis. Rectal prolapse in children may sometimes require surgery. Rectal "
    "prolapse in children with cystic fibrosis is less common than it was in the past, which may be due to earlier "
    "testing, diagnosis and treatment of cystic fibrosis. If you or your child has symptoms of cystic fibrosis - or "
    "if someone in your family has cystic fibrosis - talk with your doctor about testing for the disease. Seek "
    "immediate medical care if you or your child has difficulty breathing. Causes In cystic fibrosis, "
    "a defect (mutation) in a gene changes a protein that regulates the movement of salt in and out of cells. The "
    "result is thick, sticky mucus in the respiratory, digestive and reproductive systems, as well as increased salt "
    "in sweat. Many different defects can occur in the gene. The type of gene mutation is associated with the "
    "severity of the condition. Children need to inherit one copy of the gene from each parent in order to have the "
    "disease. If children inherit only one copy, they won't develop cystic fibrosis. However, they will be carriers "
    "and possibly pass the gene to their own children. Risk factors - Family history. Because cystic fibrosis is an "
    "inherited disorder, it runs in families. - Race. Although cystic fibrosis occurs in all races, it is most common "
    "in white people of Northern European ancestry. Complications - Damaged airways (bronchiectasis). Cystic fibrosis "
    "is one of the leading causes of bronchiectasis, a condition that damages the airways. This makes it harder to "
    "move air in and out of the lungs and clear mucus from the airways (bronchial tubes). - Chronic infections. Thick "
    "mucus in the lungs and sinuses provides an ideal breeding ground for bacteria and fungi. People with cystic "
    "fibrosis may often have sinus infections, bronchitis or pneumonia. - Growths in the nose (nasal polyps). Because "
    "the lining inside the nose is inflamed and swollen, it can develop soft, fleshy growths (polyps). - Coughing up "
    "blood (hemoptysis). Over time, cystic fibrosis can cause thinning of the airway walls. As a result, "
    "teenagers and adults with cystic fibrosis may cough up blood. - Pneumothorax. This condition, in which air "
    "collects in the space that separates the lungs from the chest wall, also is more common in older people with "
    "cystic fibrosis. Pneumothorax can cause chest pain and breathlessness. - Respiratory failure. Over time, "
    "cystic fibrosis can damage lung tissue so badly that it no longer works. Lung function usually worsens "
    "gradually, and it eventually can become life-threatening. - Acute exacerbations. People with cystic fibrosis may "
    "experience worsening of their respiratory symptoms, such as coughing and shortness of breath, for several days "
    "to weeks. This is called an acute exacerbation and requires treatment in the hospital. - Nutritional "
    "deficiencies. Thick mucus can block the tubes that carry digestive enzymes from your pancreas to your "
    "intestines. Without these enzymes, your body can't absorb protein, fats or fat-soluble vitamins. - Diabetes. The "
    "pancreas produces insulin, which your body needs to use sugar. Cystic fibrosis increases the risk of diabetes. "
    "Around 30 percent of people with cystic fibrosis develop diabetes by age 30. - Blocked bile duct. The tube that "
    "carries bile from your liver and gallbladder to your small intestine may become blocked and inflamed, "
    "leading to liver problems and sometimes gallstones. - Intestinal obstruction. Intestinal obstruction can happen "
    "to people with cystic fibrosis at all ages. Children and adults with cystic fibrosis are more likely than are "
    "infants to develop intussusception, a condition in which a section of the intestines folds in on itself like an "
    "accordion. - Distal intestinal obstruction syndrome (DIOS). DIOS is partial or complete obstruction where the "
    "small intestine meets the large intestine. Almost all men with cystic fibrosis are infertile because the tube "
    "that connects the testes and prostate gland (vas deferens) is either blocked with mucus or missing entirely. "
    "Certain fertility treatments and surgical procedures sometimes make it possible for men with cystic fibrosis to "
    "become biological fathers. Although women with cystic fibrosis may be less fertile than other women, "
    "it's possible for them to conceive and to have successful pregnancies. Still, pregnancy can worsen the signs and "
    "symptoms of cystic fibrosis, so be sure to discuss the possible risks with your doctor. - Thinning of the bones "
    "(osteoporosis). People with cystic fibrosis are at higher risk of developing a dangerous thinning of bones. - "
    "Electrolyte imbalances and dehydration. Because people with cystic fibrosis have saltier sweat, the balance of "
    "minerals in their blood may be upset. Signs and symptoms include increased heart rate, fatigue, weakness and low "
    "blood pressure. Diagnosis To diagnose cystic fibrosis, doctors may conduct several tests. Newborn screening and "
    "diagnosis Every state in the U.S. now routinely screens newborns for cystic fibrosis. Early diagnosis means "
    "treatment can begin immediately. In one screening test, a blood sample is checked for higher than normal levels "
    "of a chemical (immunoreactive trypsinogen, or IRT) released by the pancreas. A newborn's IRT levels may be high "
    "because of premature birth or a stressful delivery. For that reason other tests may be needed to confirm a "
    "diagnosis of cystic fibrosis. Genetic tests may be used in addition to checking the IRT levels to confirm the "
    "diagnosis. Doctors may also conduct genetic tests to test for specific defects on the gene responsible for "
    "cystic fibrosis. To evaluate if an infant has cystic fibrosis, doctors may also conduct a sweat test when the "
    "infant is at least 2 weeks old. In a sweat test, doctors apply a sweat-producing chemical to a small area of "
    "skin. They then collect the sweat to test it and see if it's saltier than normal. Testing may be done at a "
    "center specializing in cystic fibrosis. Testing of older children and adults Cystic fibrosis tests may be "
    "recommended for older children and adults who weren't screened at birth. Your doctor may suggest genetic and "
    "sweat tests for cystic fibrosis if you have recurring bouts of inflamed pancreas (pancreatitis), nasal polyps, "
    "chronic sinus or lung infections, bronchiectasis, or male infertility. Treatment There is no cure for cystic "
    "fibrosis, but treatment can ease symptoms and reduce complications. Close monitoring and early, aggressive "
    "intervention is recommended. Managing cystic fibrosis is complex, so consider obtaining treatment at a center "
    "staffed by doctors and other staff trained in cystic fibrosis. Doctors may work with a multidisciplinary team of "
    "doctors and medical professionals trained in cystic fibrosis to evaluate and treat your condition. The goals of "
    "treatment include: - Preventing and controlling infections that occur in the lungs - Removing and loosening "
    "mucus from the lungs - Treating and preventing intestinal blockage - Providing adequate nutrition Medications "
    "The options may include: - Antibiotics to treat and prevent lung infections - Anti-inflammatory medications to "
    "lessen swelling in the airways in your lungs - Mucus-thinning drugs to help you cough up the mucus, "
    "which can improve lung function - Inhaled medications called bronchodilators that can help keep your airways "
    "open by relaxing the muscles around your bronchial tubes - Oral pancreatic enzymes to help your digestive tract "
    "absorb nutrients For those with cystic fibrosis who have certain gene mutations, doctors may recommend a newer "
    "medication called ivacaftor (Kalydeco). This medication may improve lung function and weight, and reduce the "
    "amount of salt in sweat. It has been approved by the Food and Drug Administration for people with cystic "
    "fibrosis who are age 6 and older. The dose depends on your weight and age. Doctors may conduct liver function "
    "tests and eye examinations before prescribing ivacaftor and on a regular basis while you're taking it to check "
    "for side effects such as liver function abnormalities and cataracts. For people with a certain gene mutation who "
    "are age 12 and older, another drug (Orkambi) is available that combines ivacaftor with a medication called "
    "lumacaftor. The combination of these medications may improve lung function and reduce the risk of exacerbations. "
    "However, some people may experience side effects such as chest discomfort and shortness of breath soon after "
    "starting the medication. Some people may also have high blood pressure while taking the medication. Doctors may "
    "monitor you for any side effects. Chest physical therapy Loosening the thick mucus in the lungs makes it easier "
    "to cough up. Chest physical therapy helps loosen mucus. It is usually done from one to four times a day. A "
    "common technique is clapping with cupped hands on the front and back of the chest. Certain breathing techniques "
    "also may be used to help loosen the mucus. Your doctor will instruct you about the type of chest physical "
    "therapy he or she recommends for you. Mechanical devices also can help loosen lung mucus. These include a "
    "vibrating vest or a tube or mask you breathe into. Pulmonary rehabilitation Your doctor may recommend a "
    "long-term program that may improve your lung function and overall well-being. Pulmonary rehabilitation is "
    "usually done on an outpatient basis and may include: - Physical exercise that may improve your condition - "
    "Breathing techniques that may help loosen mucus and improve breathing - Nutritional counseling - Counseling and "
    "support - Education about your condition Surgical and other procedures - Nasal polyp removal. Your doctor may "
    "recommend surgery to remove nasal polyps that obstruct breathing. - Oxygen therapy. If your blood oxygen level "
    "declines, your doctor may recommend that you breathe pure oxygen to prevent high blood pressure in the lungs ("
    "pulmonary hypertension). - Endoscopy and lavage. Mucus may be suctioned from obstructed airways through an "
    "endoscope. - Feeding tube. Cystic fibrosis interferes with digestion, so you can't absorb nutrients from food "
    "very well. Your doctor may suggest temporarily using a feeding tube to deliver extra nutrition while you sleep. "
    "This tube may be inserted in your nose and guided to your stomach, or it may be surgically implanted into the "
    "abdomen. - Bowel surgery. If a blockage develops in your bowel, you may need surgery to remove it. "
    "Intussusception, where a section of bowel has folded in on itself, also may require surgical repair. - Lung "
    "transplant. If you have severe breathing problems, life-threatening lung complications or increasing resistance "
    "to antibiotics used to treat lung infections, lung transplantation may be an option. Because bacteria line the "
    "airways in diseases that cause permanent widening of the large airways (bronchiectasis), such as cystic "
    "fibrosis, both lungs need to be replaced. Cystic fibrosis does not recur in transplanted lungs. However, "
    "other complications associated with cystic fibrosis - such as sinus infections, diabetes, pancreas problems and "
    "osteoporosis - can still occur after a lung transplant. Lifestyle and home remedies You can manage your "
    "condition and minimize complications in several ways. Always talk to your doctor before starting home remedies. "
    "Cystic fibrosis can cause malnourishment because the enzymes needed for digestion can't reach your small "
    "intestine, preventing food from being absorbed. People with cystic fibrosis may need a significantly higher "
    "number of calories daily than do people without the condition. A healthy diet is important to maintain good lung "
    "function. It's also important to drink lots of fluids, which can help thin the mucus in your lungs. You may work "
    "with a dietitian to develop a nutrition plan. Most people with cystic fibrosis need to take pancreatic enzyme "
    "capsules with every meal and snack. In addition, your doctor may recommend: - Antacids - Supplemental "
    "high-calorie nutrition - Special fat-soluble vitamins - Extra fiber to prevent intestinal blockage - Extra salt, "
    "especially during hot weather or before exercising - Adequate water during hot weather In addition to other "
    "usual childhood vaccines, people with cystic fibrosis should have the annual flu vaccine and any other vaccines "
    "their doctor recommends. Cystic fibrosis doesn't affect the immune system, but children with cystic fibrosis are "
    "more likely to develop complications when they become sick. Regular exercise helps loosen mucus in your airways, "
    "and strengthens your heart. For many people with cystic fibrosis, participating in sports can improve confidence "
    "and self-esteem. Anything that gets you moving, including walking and biking, can help. Don't smoke in your home "
    "or car, and don't allow other people to smoke around you or your child. Secondhand smoke is harmful for "
    "everyone, but especially for people with cystic fibrosis. Teach all the members of your family to wash their "
    "hands thoroughly before eating, after using the bathroom, when coming home from work or school, and after being "
    "around a person who is sick. Hand-washing is the best way to protect against infection. You'll have ongoing care "
    "from your doctor and other medical professionals. Make sure to attend your regular follow-up appointments. Take "
    "your medications as prescribed and follow therapies as instructed. Contact your doctor if you experience any "
    "signs or symptoms such as severe constipation, more mucus than usual, blood in your mucus or reduced energy. ")

for sentence in a:
    print(sentence.ner())
# result = para_clustering(para=a, clusters=3)
# with open(LINK_TO_TEMPLATE_FILE, 'w+') as f:
#     for para in result:
#         count += 1
#         print(str(count))
#         print(str(para))
from base_type import Paragrapth, Sentence
# from preprocessing import AgglomerativeClustering, LINK_TO_INPUT
# import json
#
#
# def get_key(sentence):
#     return [word for (word, pos) in sentence.tag() if pos[0] in ['N', 'W']]
#
#
# questions = Paragrapth()
#
# data = json.load(open(LINK_TO_INPUT, mode='r'))
# for ques_id in data:
#     questions += Sentence(data[ques_id]["question"])
#
# # f = AgglomerativeClustering(questions)
#
#
# for question in questions:
#     print(question)
#     print(get_key(question))
#
