import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from flask import Flask
from threading import Thread

# ---------------------------
# FLASK WEB ENDPOINT FOR MONITORING
# ---------------------------
app = Flask(__name__)

@app.route('/')
def index():
    return "OK"

def run_flask():
    app.run(host="0.0.0.0", port=5000)

# ---------------------------
# BOT TOKEN
# ---------------------------
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
# Remove accidental spaces from secret
if TOKEN:
    TOKEN = "".join(TOKEN.split())

if not TOKEN:
    TOKEN = "8481547127:AAExYqz4UQ9XAmdWgCHKu549L0ZroGpd1Lk"

bot = telebot.TeleBot(TOKEN)

# ---------------------------
# CONTENT
# ---------------------------

CLAVICLE = """🦴 Clavicle (Right Side)
The clavicle, or collarbone, is an S-shaped long bone that connects the upper limb to the trunk. On the right side, it runs horizontally from the sternum at the center of the chest to the acromion of the shoulder, acting like a rigid support bar that keeps the shoulder away from the chest, allowing maximum arm movement. Its medial end is enlarged and triangular, articulating with the manubrium of the sternum at the sternoclavicular joint, while the lateral end is flattened and joins the acromion of the scapula at the acromioclavicular joint. These articulations are critical because they transmit forces from the upper limb to the axial skeleton, and injuries here, such as dislocations, are clinically significant.
The shaft of the clavicle is curved: the medial two-thirds bulge forward (convex anteriorly), while the lateral third curves backward (concave anteriorly). This double curvature increases resilience and allows it to absorb shocks, making it the first bone to fracture when the shoulder is impacted. On the superior surface, which lies just beneath the skin, the clavicle is smooth and easily palpable—an important landmark for procedures like central line insertion. The inferior surface is rough, providing attachments for strong ligaments. The conoid tubercle and trapezoid line near the lateral end attach the coracoclavicular ligament, which suspends the scapula, while the costoclavicular ligament at the medial end anchors the clavicle to the first rib, limiting excessive shoulder elevation. Clinically, fractures often occur in the middle third, and because the bone protects the subclavian vessels and brachial plexus, displacement can cause vascular or nerve injuries. Unlike other long bones, the clavicle has no medullary cavity, consisting of spongy bone with a thin cortical shell."""

SCAPULA = """🦴 Scapula (Right Side)
The scapula, or shoulder blade, is a flat triangular bone that lies on the posterolateral chest wall, over ribs 2 to 7 on the right side. It serves as the base from which the arm moves, gliding on the thoracic wall at the scapulothoracic “joint.” Its posterior (back) surface is divided by the spine into a smaller supraspinous fossa above and a larger infraspinous fossa below, both providing attachment to the rotator cuff muscles, which stabilize the shoulder during movement. The anterior (front) surface, facing the ribs, forms the subscapular fossa for the subscapularis muscle.
Laterally, the scapula ends in the glenoid cavity, a shallow socket that articulates with the head of the humerus, forming the glenohumeral joint. On the right side, this cavity faces slightly forward, outward, and upward. Its shallow nature explains why the shoulder is prone to dislocations. Just above the glenoid is the coracoid process, a hook-like anterior projection that serves as an attachment for the coracoclavicular ligament, which passively suspends the shoulder, and for muscles like the short head of the biceps and pectoralis minor. The acromion, an extension of the spine, forms the point of the shoulder and articulates with the clavicle at the AC joint, a common site of trauma.
The scapula has three borders: the medial (vertebral) border runs parallel to the spine and is easily palpated; the lateral (axillary) border is thick and strong, bearing stress during arm movement; and the superior border, which is thin and short, contains the suprascapular notch for passage of the suprascapular nerve. Its three angles—the superior, inferior, and lateral (glenoid)—serve as key landmarks. The inferior angle moves laterally and upward during arm elevation, an indicator of proper scapulohumeral rhythm.
High-yield clinical points include: the glenoid cavity’s shallow depth, which allows mobility but predisposes to anterior shoulder dislocations; the suprascapular notch, which can compress the nerve causing weakness of the supraspinatus and infraspinatus; and the lateral border, which is stress-resistant but can be fractured during high-energy trauma. Muscle attachments and movement patterns of the scapula are crucial for understanding shoulder mechanics and rehab protocols."""

HUMERUS = """🦴 Humerus (Right Side)
The humerus is the longest and largest bone of the upper limb, extending from the shoulder to the elbow. On the right side, it connects proximally with the scapula at the glenohumeral joint and distally with the radius and ulna at the elbow joint, serving as the primary lever for arm movement. Its shape and features provide attachment points for muscles that control the shoulder, arm, and forearm.
The proximal end of the humerus includes a rounded head, which faces medially, upward, and slightly backward, fitting into the shallow glenoid cavity of the scapula to form the shoulder joint. Surrounding the head is the anatomical neck, which marks the attachment of the joint capsule. Just distal to the head is the surgical neck, a narrower region that is clinically significant as a common fracture site, especially in falls onto the shoulder. On the anterior-lateral aspect of the proximal end are the greater tubercle (lateral) and the lesser tubercle (anterior), separated by the intertubercular (bicipital) groove, which houses the tendon of the long head of the biceps.
The shaft of the humerus is cylindrical proximally and becomes more triangular as it approaches the distal end. Laterally, it has the deltoid tuberosity, where the deltoid muscle attaches, allowing abduction of the arm. On the posterior aspect, the radial (spiral) groove runs obliquely down the shaft and accommodates the radial nerve and profunda brachii artery; fractures along this part of the humerus can injure the radial nerve, resulting in wrist drop.
The distal end of the humerus expands to form the condyle, which articulates with the forearm bones. Laterally, the capitulum articulates with the head of the radius, allowing smooth flexion and extension as well as rotation during pronation and supination. Medially, the trochlea articulates with the trochlear notch of the ulna, functioning like a pulley for hinge movement at the elbow. Just above these articulating surfaces are the fossae: the radial fossa (anterior-lateral) receives the radial head during flexion, the coronoid fossa (anterior-medial) receives the coronoid process of the ulna, and the large olecranon fossa (posterior) receives the olecranon when the elbow is extended.
Prominent medial and lateral epicondyles project on either side of the distal humerus, serving as attachment points for forearm flexor and extensor muscles. High-yield clinical points include the surgical neck, prone to fractures affecting the axillary nerve and posterior circumflex humeral artery; the shaft, where fractures risk radial nerve injury; and the supracondylar region, common in children, which can compromise the brachial artery or median nerve.
On the right side, visualizing the humerus in anatomical position: the head faces medially into the glenoid cavity, the greater tubercle is lateral, the lesser tubercle is anterior, and the deltoid tuberosity is lateral mid-shaft, while the condyles at the distal end articulate anteriorly with the radius and ulna, forming the elbow hinge."""

RADIUS_ULNA = """🦴 Radius and Ulna (Right Forearm)
The forearm consists of two parallel bones, the radius and the ulna, which together form a mobile lever for positioning the hand. These bones allow flexion, extension, and rotation of the forearm, enabling pronation and supination, which are essential for hand movements. On the right side, the radius lies on the lateral (thumb) side, while the ulna is on the medial (little finger) side, with both extending from the elbow to the wrist.
The ulna is the stabilizing bone of the forearm. Its proximal end is broad and specialized for articulation with the humerus. Posteriorly, the olecranon forms the bony point of the elbow, acting as a lever for elbow extension. Anteriorly, the coronoid process projects forward to form the lower part of the trochlear notch, which grips the trochlea of the humerus like a pulley, allowing hinge-like flexion and extension. On the lateral aspect of the coronoid process lies the radial notch, where the head of the radius rotates. The shaft of the ulna is thick proximally and narrows distally, ending in a small head and a medial ulnar styloid process.
The radius is the shorter, lateral, and rotating bone of the forearm. Its proximal end has a disc-shaped head, concave superiorly, which articulates with the capitulum of the humerus to allow flexion and extension at the elbow, and peripherally with the radial notch of the ulna for pronation and supination. Just below the head is the neck, which narrows before expanding into the radial tuberosity, the attachment site for the biceps brachii tendon. The shaft of the radius gradually widens distally, where it articulates with the scaphoid and lunate carpal bones at the wrist joint. On its medial side, the ulnar notch receives the head of the ulna, while the lateral radial styloid process projects downward.
Together, the radius and ulna transmit forces from the hand to the humerus. The interosseous membrane connects the shafts of both bones obliquely, directing compressive forces from the radius to the ulna. Clinically, the distal radius is the site of Colles’ fracture, often occurring from a fall on an outstretched hand, while proximal fractures can involve the radial head, affecting forearm rotation."""

HAND_BONES = """🦴 Hand Bones (Right Hand)
The hand forms the distal part of the upper limb and is composed of carpals, metacarpals, and phalanges, allowing intricate movements, grip, and manipulation. Visualizing the right hand in anatomical position, the palm faces forward, the thumb is lateral, and the little finger is medial, extending from the distal forearm to the fingertips.
The carpus (wrist) consists of eight small bones arranged in two rows, which provide flexibility and allow gliding movements. The proximal row (from lateral/thumb side to medial/little finger side) includes the scaphoid, lunate, triquetrum, and pisiform. The distal row of carpals (lateral → medial) includes the trapezium, trapezoid, capitate, and hamate.
The metacarpals form the skeleton of the palm. Each metacarpal has a base (proximal), shaft, and head (distal). The proximal bases articulate with the distal row of carpals, while the distal heads form the knuckles with the proximal phalanges.
The phalanges are the bones of the fingers. Each finger has three phalanges—proximal, middle, and distal—except the thumb, which has only two. The distal phalanges have small, rounded tips that support the fingertips, while the proximal and middle phalanges provide structural support for finger flexion and extension.
Together, the carpals, metacarpals, and phalanges form a highly mobile and versatile structure. In the right hand, the lateral thumb side is key for precision and opposition, while the medial little finger side provides stability and grip strength."""

FASCIA = """FASCIA
Under the skin of the upper limb, there are two main layers. The first is the superficial fascia, which contains fat, and the second is the deep fascia, which surrounds muscles and divides them into compartments. In areas where nothing lies between the skin and bone, the deep fascia attaches directly to bone. In the chest, the pectoral fascia covers the pectoralis major (a major chest muscle) and attaches to the clavicle and sternum.
Beneath the pectoral fascia, the clavipectoral fascia wraps the subclavius and pectoralis minor muscles. A part of this fascia, the costocoracoid membrane, is pierced by the lateral pectoral nerve.
The scapulohumeral muscles (deltoid, supraspinatus, infraspinatus, subscapularis, teres minor) are also covered by fascia. The deltoid fascia covers the deltoid muscle and comes down from the clavicle, acromion, and scapular spine.
In the arm, the brachial fascia wraps all the arm muscles like a tight sleeve. Two intermuscular septa divide the arm into anterior (flexor) and posterior (extensor) compartments.
In the forearm, the antebrachial fascia wraps the forearm muscles. On the back of the wrist, it thickens to form the extensor retinaculum. On the front, it forms the flexor retinaculum, which creates the carpal tunnel."""

VESSELS = """VESSELS
The arterial system of the upper limb starts from the aorta on the left or the brachiocephalic trunk on the right. The subclavian artery travels under the first rib and becomes the axillary artery. At the lower edge of the teres major, it continues as the brachial artery. Near the elbow, it divides into the radial artery (thumb side) and ulnar artery (little finger side).
Superficial veins include the cephalic vein (lateral side) and the basilic vein (medial side). The median cubital vein connects them at the elbow and is commonly used for drawing blood."""

CUTANEOUS_NERVES = """CUTANEOUS NERVES
The skin of the upper limb is mainly supplied by branches of the brachial plexus (C5–T1). Key cutaneous nerves include the lateral cutaneous nerve of the forearm, medial cutaneous nerve of the forearm, posterior cutaneous nerve of the arm, and the superficial branch of the radial nerve. The shoulder also receives nerves from the cervical plexus (supraclavicular nerves C3–C4)."""

AXILLA = """THE AXILLA
The axilla or armpit, is a pyramid-shaped space between the upper arm and the chest. Its apex points toward the root of the neck. It contains the axillary artery and its branches, the axillary vein and its tributaries, the cords and branches of the brachial plexus, and lymph nodes embedded in axillary fat. All these structures are wrapped in the axillary sheath."""

CUBITAL_FOSSA = """CUBITAL FOSSA
The cubital fossa is a triangular depression in front of the elbow. Its boundaries are the brachioradialis muscle laterally and the pronator teres muscle medially. From lateral to medial, the main contents are: radial nerve, biceps brachii tendon, brachial artery, and median nerve. The median cubital vein crosses superficially."""

CARPAL_TUNNEL = """THE CARPAL TUNNEL
The carpal tunnel is a narrow passage on the palmar side of the wrist. Its floor and sides are formed by the carpal bones, and its roof by the flexor retinaculum. Inside pass nine flexor tendons and the median nerve. Compression here causes Carpal Tunnel Syndrome."""

GUYONS_CANAL = """THE GUYON'S CANAL
Guyon’s canal (ulnar canal) is a tunnel at the wrist formed by the pisiform and hamate bones. It transmits the ulnar nerve and artery into the hand. Compression here can cause ulnar nerve neuropathy."""

ANATOMICAL_SNUFFBOX = """THE ANATOMICAL SNUFFBOX
The anatomical snuffbox is a triangular depression on the dorsolateral wrist. Its borders are the tendons of abductor pollicis longus and extensor pollicis brevis laterally, and extensor pollicis longus medially. Its floor is formed by the scaphoid and trapezium bones. It contains the radial artery and cephalic vein. Tenderness here indicates possible scaphoid fracture."""

BP_FORMATION = """1. FORMATION AND TOPOGRAPHICAL ANATOMY =
The brachial plexus is a major nerve network formed by the anterior rami of C5, C6, C7, C8, and T1, providing motor and sensory innervation to almost the entire upper limb, except the trapezius (innervated by CN XI) and a small patch near the axilla supplied by the intercostobrachial nerve. The roots pass through the interscalene triangle, between the anterior and middle scalene muscles, and converge in the posterior triangle of the neck to form the trunks. The plexus continues posterior to the clavicle into the axilla, forming cords around the axillary artery, all enclosed within the axillary sheath.
Anatomical variations are common: approximately 50% of individuals have prefixed (C4 contribution) or postfixed (T2 contribution) plexuses, which are clinically significant for regional anesthesia, surgery, and potential nerve compression."""

BP_ROOTS = """2. ROOTS_(C5_T1) =
The roots are the ventral rami of the lower four cervical nerves (C5–C8) and T1. They carry motor, sensory, and sympathetic fibers and pass between the scalene muscles along with the subclavian artery. Lesions affecting a single root usually cause weakness rather than complete paralysis due to contributions from multiple roots to major nerves."""

BP_TRUNKS = """3. TRUNKS (SUPERIOR, MIDDLE, INFERIOR) =
Superior trunk: union of C5 and C6 roots
Middle trunk: continuation of C7 root
Inferior trunk: union of C8 and T1 roots
Trunks traverse laterally over the first rib and apex of the lung toward the clavicle."""

BP_DIVISIONS = """4. DIVISIONS (ANTERIOR AND POSTERIOR) =
Each trunk splits into anterior and posterior divisions. The anterior divisions supply the flexor compartments (anterior arm and forearm), while posterior divisions supply the extensor compartments (posterior arm and forearm). No named branches arise directly from divisions."""

BP_CORDS = """5. CORDS (LATERAL, MEDIAL, POSTERIOR) =
The six divisions recombine in the axilla to form three cords:
Lateral cord: anterior divisions of superior and middle trunks (C5–C7)
Medial cord: anterior division of the inferior trunk (C8–T1)
Posterior cord: union of all posterior divisions (C5–T1)
Cords give rise to collateral branches and the five major terminal nerves of the upper limb."""

BP_SUPRACLAVICULAR = """6. SUPRACLAVICULAR BRANCHES (FROM ROOTS & TRUNKS) =
These branches arise proximal to the clavicle and primarily innervate scapular and periscapular muscles:
Dorsal scapular nerve (C5): Levator scapulae, rhomboid major and minor
Long thoracic nerve (C5–C7): Serratus anterior, vulnerable to injury during axillary surgery
Nerve to subclavius (C5–C6): Stabilizes clavicle
Suprascapular nerve (C5–C6): Supraspinatus, infraspinatus, and glenohumeral joint."""

BP_INFRACLAVICULAR = """7. INFRACLAVICULAR BRANCHES (FROM CORDS)=
Lateral Cord (C5–C7) – “Lucy Loves Me”:
Lateral pectoral nerve: Clavicular head of pectoralis major
Musculocutaneous nerve: Coracobrachialis, biceps, brachialis; continues as lateral cutaneous nerve of forearm
Lateral root of median nerve: Joins medial root to form median nerve
Medial Cord (C8–T1) – “Most Medical Men Use Morphine”:
Medial pectoral nerve: Sternocostal head of pectoralis major, pectoralis minor
Medial cutaneous nerves of arm and forearm: Sensory
Ulnar nerve: Flexor carpi ulnaris, medial half of flexor digitorum profundus, most intrinsic hand muscles
Medial root of median nerve: Joins lateral root to form median nerve
Posterior Cord (C5–T1) – “STAR/ULTRA”:
Upper subscapular nerve: Superior subscapularis
Thoracodorsal nerve: Latissimus dorsi
Lower subscapular nerve: Inferior subscapularis, teres major
Axillary nerve: Deltoid, teres minor, shoulder joint, upper lateral cutaneous nerve of arm
Radial nerve: All posterior arm & forearm muscles, posterior cutaneous branches."""

BP_TERMINAL = """8. MAJOR TERMINAL NERVES & BRANCHES=
Musculocutaneous (C5–C7): Coracobrachialis, biceps, brachialis; lateral forearm sensation
Median (C5–T1): Flexor muscles of forearm, lateral half of hand, carpal tunnel
Ulnar (C8–T1): Flexor carpi ulnaris, medial flexor digitorum profundus, intrinsic hand muscles
Radial (C5–T1): Triceps, extensors of forearm, posterior forearm & hand skin
Axillary (C5–C6): Deltoid, teres minor, regimental badge area, shoulder joint."""

MUSCLES_VERTEBRAL = """💪 Muscles Connecting the Upper Limb to the Vertebral Column
Trapezius
Origin: Occipital bone, ligamentum nuchae, spinous processes of C7 and all thoracic vertebrae
Insertion: Upper fibers → lateral third of clavicle; Middle & lower fibers → acromion and scapular spine
Nerve supply: Spinal accessory nerve (CN XI), C3–C4
Action: Upper fibers elevate scapula, middle fibers retract, lower fibers depress medial border

Latissimus dorsi
Origin: Spinous processes of lower six thoracic vertebrae, lumbar & sacral vertebrae, iliac crest, slips from lower four ribs
Insertion: Floor of intertubercular groove of humerus
Nerve supply: Thoracodorsal nerve
Action: Extends, adducts, and medially rotates arm

Levator scapulae
Origin: Transverse processes of upper four cervical vertebrae
Insertion: Medial border of scapula
Nerve supply: C3–C4, dorsal scapular nerve
Action: Raises medial border of scapula

Rhomboid minor
Origin: Ligamentum nuchae, spinous processes of C7 and T1
Insertion: Medial border of scapula
Nerve supply: Dorsal scapular nerve
Action: Elevates medial border of scapula upward and medially

Rhomboid major
Origin: Spinous processes of T2–T5
Insertion: Medial border of scapula
Nerve supply: Dorsal scapular nerve
Action: Elevates medial border of scapula upward and medially"""

MUSCLES_THORACIC = """💪 Muscles Connecting the Upper Limb to the Thoracic Wall
Pectoralis major
Origin: Clavicle, sternum, upper six costal cartilages
Insertion: Lateral lip of bicipital groove of humerus
Nerve supply: Medial & lateral pectoral nerves (brachial plexus)
Action: Adducts and medially rotates arm; clavicular fibers flex arm

Pectoralis minor
Origin: 3rd–5th ribs
Insertion: Coracoid process of scapula
Nerve supply: Medial pectoral nerve
Action: Depresses shoulder; if scapula fixed, elevates ribs

Subclavius
Origin: First costal cartilage
Insertion: Clavicle
Nerve supply: Nerve to subclavius (upper trunk of brachial plexus)
Action: Depresses and stabilizes clavicle

Serratus anterior
Origin: Upper eight ribs
Insertion: Medial border and inferior angle of scapula
Nerve supply: Long thoracic nerve
Action: Draws scapula forward, rotates it"""

MUSCLES_SCAPULA_HUMERUS = """💪 Muscles Connecting the Scapula to the Humerus
Deltoid
Origin: Lateral third of clavicle, acromion, spine of scapula
Insertion: Deltoid tuberosity of humerus
Nerve supply: Axillary nerve
Action: Abducts arm; anterior fibers flex & medially rotate, posterior fibers extend & laterally rotate

Supraspinatus
Origin: Supraspinous fossa of scapula
Insertion: Greater tuberosity of humerus, shoulder capsule
Nerve supply: Suprascapular nerve
Action: Abducts arm, stabilizes shoulder

Infraspinatus
Origin: Infraspinous fossa of scapula
Insertion: Greater tuberosity of humerus, shoulder capsule
Nerve supply: Suprascapular nerve
Action: Laterally rotates arm, stabilizes shoulder

Teres major
Origin: Lower third of lateral border of scapula
Insertion: Medial lip of bicipital groove of humerus
Nerve supply: Lower subscapular nerve
Action: Medially rotates, adducts, stabilizes arm

Teres minor
Origin: Upper two-thirds of lateral border of scapula
Insertion: Greater tuberosity of humerus
Nerve supply: Axillary nerve
Action: Laterally rotates arm, stabilizes shoulder

Subscapularis
Origin: Subscapular fossa
Insertion: Lesser tuberosity of humerus
Nerve supply: Upper & lower subscapular nerves
Action: Medially rotates arm, stabilizes shoulder"""

MUSCLES_ARM_ANTERIOR = """💪 Muscles of the Upper Arm - Anterior Compartment (Flexors)
Biceps brachii
Long head
Origin: Supraglenoid tubercle of scapula
Insertion: Radial tuberosity & bicipital aponeurosis
Nerve: Musculocutaneous nerve
Action: Supinates forearm, flexes elbow, weak shoulder flexion
Short head
Origin: Coracoid process of scapula
Other details same as long head

Coracobrachialis
Origin: Coracoid process
Insertion: Medial humeral shaft
Nerve: Musculocutaneous nerve
Action: Flexes arm, weak adduction

Brachialis
Origin: Lower anterior humerus
Insertion: Coronoid process of ulna
Nerve: Musculocutaneous nerve
Action: Flexes elbow"""

MUSCLES_ARM_POSTERIOR = """💪 Muscles of the Upper Arm - Posterior Compartment (Extensors)
Triceps brachii
Long head
Origin: Infraglenoid tubercle of scapula
Insertion: Olecranon
Nerve: Radial nerve
Action: Extends elbow, assists shoulder extension
Lateral head
Origin: Upper posterior humerus
Insertion & nerve: Same as long head
Action: Extends elbow
Medial head
Origin: Lower posterior humerus
Insertion & nerve: Same as long head
Action: Extends elbow"""

MUSCLES_FOREARM_ANTERIOR = """💪 Muscles of the Forearm - Anterior Fascial Compartment (Flexors & Pronators)
Pronator teres
Origin: Medial epicondyle of humerus & coronoid process of ulna
Insertion: Lateral aspect of radius
Nerve: Median nerve
Action: Pronates and flexes forearm

Flexor carpi radialis
Origin: Medial epicondyle of humerus
Insertion: Base of 2nd metacarpal
Nerve: Median nerve
Action: Flexes & abducts hand at wrist

Palmaris longus
Origin: Medial epicondyle of humerus
Insertion: Palmar aponeurosis
Nerve: Median nerve
Action: Flexes hand

Flexor carpi ulnaris
Origin: Medial epicondyle of humerus, olecranon, posterior ulna
Insertion: Pisiform bone, hook of hamate, base of 5th metacarpal
Nerve: Ulnar nerve
Action: Flexes and adducts hand at wrist

Flexor digitorum superficialis
Origin: Medial epicondyle, coronoid process of ulna, oblique line of radius
Insertion: Middle phalanges of medial four fingers
Nerve: Median nerve
Action: Flexes middle phalanges of fingers, then proximal phalanges and hand

Flexor digitorum profundus
Origin: Anteromedial surface of ulna & interosseous membrane
Insertion: Bases of distal phalanges of medial four fingers
Nerve: Ulnar nerve (medial half) & Median nerve (lateral half)
Action: Flexes distal phalanges of fingers

Flexor pollicis longus
Origin: Anterior surface of radius & interosseous membrane
Insertion: Base of distal phalanx of thumb
Nerve: Median nerve
Action: Flexes distal phalanx of thumb

Pronator quadratus
Origin: Lower quarter of anterior surface of ulna
Insertion: Lower quarter of anterior surface of radius
Nerve: Median nerve
Action: Pronates forearm"""

MUSCLES_FOREARM_POSTERIOR = """💪 Muscles of the Forearm - Posterior Fascial Compartment (Extensors & Supinators)
Brachioradialis
Origin: Lateral supracondylar ridge of humerus
Insertion: Lateral surface of distal radius
Nerve: Radial nerve
Action: Flexes forearm (midprone position)

Extensor carpi radialis longus
Origin: Lateral supracondylar ridge of humerus
Insertion: Base of 2nd metacarpal
Nerve: Radial nerve
Action: Extends & abducts hand at wrist

Extensor carpi radialis brevis
Origin: Lateral epicondyle of humerus
Insertion: Base of 3rd metacarpal
Nerve: Radial nerve
Action: Extends & abducts hand at wrist

Extensor digitorum
Origin: Lateral epicondyle of humerus
Insertion: Extensor expansion of medial four fingers
Nerve: Radial nerve
Action: Extends fingers and hand

Extensor digiti minimi
Origin: Lateral epicondyle of humerus
Insertion: Extensor expansion of little finger
Nerve: Radial nerve
Action: Extends little finger

Extensor carpi ulnaris
Origin: Lateral epicondyle of humerus & posterior surface of ulna
Insertion: Base of 5th metacarpal
Nerve: Radial nerve
Action: Extends and adducts hand at wrist

Anconeus
Origin: Lateral epicondyle of humerus
Insertion: Olecranon & posterior surface of ulna
Nerve: Radial nerve
Action: Assists triceps in elbow extension, stabilizes elbow

Supinator
Origin: Lateral epicondyle & supinator fossa of ulna
Insertion: Neck and shaft of radius
Nerve: Radial nerve
Action: Supinates forearm

Abductor pollicis longus
Origin: Posterior surfaces of radius, ulna, interosseous membrane
Insertion: Base of 1st metacarpal
Nerve: Radial nerve
Action: Abducts and extends thumb

Extensor pollicis brevis
Origin: Posterior surface of radius & interosseous membrane
Insertion: Base of proximal phalanx of thumb
Nerve: Radial nerve
Action: Extends proximal phalanx of thumb

Extensor pollicis longus
Origin: Posterior surface of ulna & interosseous membrane
Insertion: Base of distal phalanx of thumb
Nerve: Radial nerve
Action: Extends distal phalanx of thumb

Extensor indicis
Origin: Posterior surface of ulna & interosseous membrane
Insertion: Extensor expansion of index finger
Nerve: Radial nerve
Action: Extends index finger"""

MUSCLES_HAND = """💪 Small Muscles of the Hand
Thenar Muscles (Thumb)
- Abductor pollicis brevis: Abducts thumb
- Flexor pollicis brevis: Flexes thumb
- Opponens pollicis: Opposes thumb
Nerve: Median nerve (except deep head of flexor pollicis brevis, which is ulnar)

Hypothenar Muscles (Little Finger)
- Abductor digiti minimi: Abducts little finger
- Flexor digiti minimi brevis: Flexes little finger
- Opponens digiti minimi: Opposes little finger
Nerve: Ulnar nerve

Adductor Pollicis
Origin: 2nd & 3rd metacarpals, capitate bone
Insertion: Base of proximal phalanx of thumb
Nerve: Ulnar nerve
Action: Adducts thumb

Lumbrical Muscles (4)
Origin: Tendons of flexor digitorum profundus
Insertion: Extensor expansions of medial four fingers
Nerve: 1st & 2nd (Median), 3rd & 4th (Ulnar)
Action: Flex metacarpophalangeal joints, extend interphalangeal joints

Interossei Muscles
- Palmar interossei (3): Adduct fingers
- Dorsal interossei (4): Abduct fingers
Nerve: Ulnar nerve
Action: Also assist lumbricals in flexing MP and extending IP joints"""

ROTATOR_CUFF_OVERVIEW = """The Rotator Cuff (SITS)
The rotator cuff is a group of four muscles that stabilize the shoulder joint (glenohumeral joint) by holding the head of the humerus in the shallow glenoid cavity of the scapula. These muscles are:
1. Supraspinatus
2. Infraspinatus
3. Teres Minor
4. Subscapularis
(Mnemonic: SITS)
They form a "cuff" around the joint and are essential for shoulder mobility and stability."""

MUSCLE_SUPRASPINATUS = """Supraspinatus
Origin: Supraspinous fossa of scapula
Insertion: Greater tuberosity of humerus (top facet)
Nerve supply: Suprascapular nerve (C5-C6)
Action: Initiates abduction of the arm (first 15 degrees) and stabilizes the shoulder joint."""

MUSCLE_INFRASPINATUS = """Infraspinatus
Origin: Infraspinous fossa of scapula
Insertion: Greater tuberosity of humerus (middle facet)
Nerve supply: Suprascapular nerve (C5-C6)
Action: Lateral rotation of the arm and stabilizes the shoulder joint."""

MUSCLE_TERES_MINOR = """Teres Minor
Origin: Upper two-thirds of the lateral border of the scapula
Insertion: Greater tuberosity of humerus (lower facet)
Nerve supply: Axillary nerve (C5-C6)
Action: Lateral rotation of the arm and stabilizes the shoulder joint."""

MUSCLE_SUBSCAPULARIS = """Subscapularis
Origin: Subscapular fossa of scapula (anterior surface)
Insertion: Lesser tuberosity of humerus
Nerve supply: Upper and lower subscapular nerves (C5-C6)
Action: Medial rotation of the arm and stabilizes the shoulder joint."""

JOINT_SHOULDER = """THE SHOULDER JOINT (Glenohumeral Joint)
Type: Synovial ball-and-socket joint
Articulating surfaces: Head of humerus and glenoid cavity of scapula

Capsule: Loose, allows wide range of motion. Weakest inferiorly.

Ligaments:
- Glenohumeral ligaments (superior, middle, inferior)
- Coracohumeral ligament
- Transverse humeral ligament (holds biceps tendon)

Bursae: Subacromial (subdeltoid), subscapular bursae

Movements:
- Flexion: Pectoralis major (clavicular), deltoid (anterior), coracobrachialis
- Extension: Latissimus dorsi, teres major, deltoid (posterior)
- Abduction: Supraspinatus (0-15°), deltoid (15-90°), serratus anterior & trapezius (>90°)
- Adduction: Pectoralis major, latissimus dorsi, teres major
- Medial rotation: Subscapularis, pectoralis major, latissimus dorsi, teres major
- Lateral rotation: Infraspinatus, teres minor, deltoid (posterior)

Stability provided by: Rotator cuff muscles (SITS), long head of biceps, glenoid labrum.
Clinical notes: Dislocation (mostly anterior), Rotator cuff tears."""

JOINT_ELBOW = """THE ELBOW JOINT
Type: Synovial hinge joint
Articulating surfaces:
1. Trochlea of humerus with trochlear notch of ulna
2. Capitulum of humerus with head of radius

Capsule: Encloses the joint

Ligaments:
- Lateral (radial) collateral ligament: Lateral epicondyle → annular ligament & ulna
- Medial (ulnar) collateral ligament: Medial epicondyle → coronoid process & olecranon

Movements:
- Flexion: Brachialis, biceps brachii, brachioradialis
- Extension: Triceps brachii, anconeus

Clinical notes: Elbow dislocation, Supracondylar fracture (brachial artery risk)."""

JOINT_RADIOULNAR = """RADIOULNAR JOINTS
1. Proximal Radioulnar Joint (Elbow area): Pivot joint. Head of radius with radial notch of ulna. Held by annular ligament.
2. Distal Radioulnar Joint (Wrist area): Pivot joint. Head of ulna with ulnar notch of radius.
3. Middle Radioulnar Joint: Fibrous joint (interosseous membrane).

Movements:
- Supination: Biceps brachii (primary when elbow flexed), supinator
- Pronation: Pronator teres, pronator quadratus

Clinical notes: Pulled elbow (subluxation of radial head in children)."""

JOINT_WRIST = """THE WRIST JOINT (Radiocarpal Joint)
Type: Synovial ellipsoid joint
Articulating surfaces: Distal radius and triangular fibrocartilage disc with scaphoid, lunate, and triquetrum bones. (Note: Ulna does NOT articulate directly with carpal bones).

Ligaments: Palmar & dorsal radiocarpal, ulnar & radial collateral ligaments.

Movements:
- Flexion: Flexor carpi radialis, flexor carpi ulnaris, flexor digitorum
- Extension: Extensor carpi radialis (longus/brevis), extensor carpi ulnaris, extensor digitorum
- Abduction (radial deviation): Flexor carpi radialis, extensor carpi radialis
- Adduction (ulnar deviation): Flexor carpi ulnaris, extensor carpi ulnaris

Clinical notes: Colles' fracture, Scaphoid fracture."""

JOINT_HAND = """JOINTS OF THE HAND
1. Intercarpal joints: Plane synovial joints (gliding).
2. Carpometacarpal (CMC) joints:
   - Thumb CMC: Saddle joint (allows opposition).
   - Others: Plane synovial joints.
3. Metacarpophalangeal (MCP) joints: Condyloid joints (flexion, extension, abduction, adduction).
4. Interphalangeal (IP) joints: Hinge joints (flexion, extension)."""

CLINICAL_FRACTURES = """*Fractures*

*Scapula Fractures*
Scapula fractures are rare because the bone is well-protected by muscles. If it fractures, it usually means severe trauma, like a high-speed car accident, crushing injuries, or sports injuries. The surrounding muscles usually hold the pieces together, so treatment is often conservative.

*Clavicle Fractures*
The clavicle transmits forces from the arm to the trunk. It is most commonly fractured when someone falls on the shoulder or outstretched hand.
Lateral third fractures make up 15%
Middle third fractures are 80%
Medial third fractures are 5%
After fracture, the lateral end is pulled down by the arm weight and medially by pectoralis major, while the medial end is pulled up by the sternocleidomastoid. Treatment can be a sling or surgery (ORIF). Surgery may damage supraclavicular nerves, causing a numb patch over the shoulder.

*Humerus Fractures*
*Surgical Neck:* Usually from a fall or direct blow. Axillary nerve and posterior circumflex artery are at risk. Damage to axillary nerve causes paralysis of deltoid and teres minor, and numbness over the “regimental badge” area (upper lateral [outer] arm).
*Mid-Shaft:* Risk of radial nerve injury and profunda brachii artery damage. Radial nerve damage causes paralysis of wrist extensors, producing wrist drop, and some sensory loss on the back of the arm and lateral (outer) three and a half fingers.
*Supracondylar:* Common in children from falling on an outstretched hand. May damage brachial artery, causing Volkmann’s ischemic contracture (hand flexion due to shortened flexor muscles). May also injure anterior interosseous nerve, ulnar, or radial nerves.

*Ulna Fractures*
Shaft fractures occur from a direct blow. The proximal part may be pulled back by muscles.
Olecranon fractures occur when falling on a flexed elbow. Triceps may pull fragments upward.
Classical fracture types:
*Monteggia fracture:* Proximal ulna breaks, radial head dislocates at elbow.
*Galeazzi fracture:* Distal radius breaks, ulna dislocates at wrist.

*Radius Fractures*
*Colles fracture:* Fall on outstretched hand. Distal radius fragment displaced posteriorly (toward back of hand), creating “dinner fork” deformity.
*Smith fracture:* Fall on back of hand. Distal radius fragment displaced anteriorly (toward palm).
*Radial head fracture:* From falling on outstretched hand; radial head hits humerus.

*Scaphoid Fracture*
Most common hand fracture, often from falling on an outstretched hand. Pain is felt in the anatomical snuffbox (lateral [thumb side] wrist area). Blood supply is from distal (far) to proximal (near) end, so fractures can cause avascular necrosis of the proximal fragment. Missed fractures may cause wrist osteoarthritis later.

*Metacarpal Fractures*
*Boxer’s fracture:* Neck of 5th metacarpal breaks from punching a hard object; distal fragment moves forward, shortening the finger.
*Bennett fracture:* Base of 1st metacarpal breaks from forced thumb hyperabduction; often involves the joint and may need surgery."""

CLINICAL_DISLOCATIONS = """*Dislocations and Joint Injuries*

*Shoulder Dislocations*
Most common type: Anterior dislocation (humeral head moves forward and down). Caused by excessive extension and lateral rotation of arm.
Can tear the joint capsule and damage axillary or radial nerves.
Complications: Hill-Sachs lesion (posterolateral [back and outer] humeral head compression) and Bankart lesion (detachment of anteroinferior [front and lower] labrum).

*Acromioclavicular Joint Dislocation*
Also called a separated shoulder. Usually from a direct blow to the shoulder or a fall. If the coracoclavicular ligament tears, the shoulder drops (moves downward), making the clavicle more prominent. Treatment depends on severity: rest, ice, or surgery.

*Sternoclavicular Joint Dislocation*
Rare; needs significant force. Types:
Anterior dislocation: Shoulder rotates backward.
Posterior dislocation: Shoulder moves forward.
Young people may also fracture the growth plate at the sternal end.

*Elbow Injuries*
*Bursitis:* Subcutaneous (from repeated friction) or subtendinous (from repeated flexion/extension).
*Dislocation:* Often posterior (ulna moves backward relative to humerus), from falls on a flexed elbow. May damage the ulnar nerve (medial [inner] arm).
*Epicondylitis:* Tennis elbow (lateral [outer] epicondyle) or golfer’s elbow (medial [inner] epicondyle) from overuse.
*Supracondylar fracture:* Falling on flexed elbow. Can damage brachial artery, causing Volkmann’s contracture, and nerves (median, ulnar, radial).

*Wrist Injuries*
*Scaphoid fracture:* Pain in anatomical snuffbox; risk of avascular necrosis.
*Lunate dislocation:* Moves anteriorly (toward palm), compresses carpal tunnel, causing median nerve symptoms.
*Colles fracture:* Distal radius fracture with posterior (backward) displacement; “dinner fork deformity.”"""

CLINICAL_NERVES = """*Nerve Injuries*

*Long Thoracic Nerve*
Controls serratus anterior, which holds scapula (shoulder blade) against the ribcage (back of chest).
Damage causes winged scapula, where shoulder blade sticks out. Usually from trauma or repetitive shoulder movement.

*Accessory Nerve*
Controls trapezius (upper back/neck) and sternocleidomastoid (side of neck).
Damage can occur during surgery (cervical lymph node biopsy or jugular vein cannulation).
Signs: Shoulder droop, muscle wasting, asymmetrical neckline.

*Axillary Nerve*
From surgical neck of humerus trauma.
Paralysis of deltoid and teres minor (shoulder muscles), loss of sensation over upper lateral (outer) arm (“regimental badge” area).

*Musculocutaneous Nerve*
Rarely injured; usually stab wounds.
Weak elbow flexion, weakened shoulder flexion, weakened supination.
Sensory loss over lateral (outer) forearm.

*Median Nerve*
Injury at elbow (supracondylar fracture) or wrist (laceration).
Paralysis of forearm flexors (except flexor carpi ulnaris and medial flexor digitorum profundus)
Thenar muscles affected.
*Hand of benediction* when trying to make a fist.
Sensory loss in median nerve area (lateral [thumb to middle] side of hand).

*Ulnar Nerve*
Vulnerable at elbow (medial [inner] epicondyle) or wrist.
Paralysis of interossei and medial lumbricals; cannot abduct or adduct fingers.
Long-term injury leads to *ulnar claw:* hyperextended MCP joints, flexed IP joints of ring and little fingers.
Sensory loss over medial (inner) one and a half fingers.

*Radial Nerve*
Injuries at axilla, radial groove, or forearm.
*Axilla:* triceps and wrist/finger extensors paralyzed, sensory loss lateral (outer) arm and posterior (back) forearm, wrist drop.
*Radial groove:* triceps partially affected, wrist drop occurs, sensory loss of dorsal (back) lateral hand.
*Forearm:* deep branch affects wrist/finger extensors, superficial branch affects lateral 3.5 digits."""

CLINICAL_VASCULAR = """*Vascular Injuries*

*Axillary Artery Aneurysm*
Rare; may occur due to atherosclerosis, trauma, or thoracic outlet syndrome.
Can compress brachial plexus, causing numbness, tingling, and weakness.
Treatment: surgical removal and graft reconstruction.

*Brachial Artery Laceration*
Complete blockage or severing is a medical emergency.
Can cause ischemia in forearm muscles, leading to Volkmann’s contracture (flexion deformity of hand).

*Venepuncture*
Median cubital vein is ideal for IV access due to superficial position and fixation."""

CLINICAL_MUSCLES = """*Muscle and Tendon Injuries*

*Rotator Cuff Tendonitis*
Usually supraspinatus tendon (top of shoulder).
Caused by repetitive shoulder use; tendon rubs under coracoacromial arch (bony roof of shoulder).
Pain during abduction between 60 and 120 degrees (“painful arc”).
Treatment: rest, analgesics, physiotherapy, steroid injections, or surgery.

*Subscapularis / Impingement Syndromes*
Compression or inflammation under coracoid process or acromion (front or top of shoulder) can cause pain and weakness.

*Biceps Tendon Rupture*
Usually the long head.
Bulge in muscle belly when elbow is flexed (“Popeye sign”).
Minimal weakness due to brachialis and supinator.

*Lateral Epicondylitis (Tennis Elbow)*
Overuse of superficial extensor muscles.
Pain at lateral (outer) epicondyle; peak age 40-50.

*Dupuytren Contracture*
Thickened palmar fascia causing finger flexion.
Fingers cannot fully extend; gripping objects is difficult.
Often hereditary; treated surgically."""

CLINICAL_SPECIAL = """*Special Conditions*

*Compartment Syndrome*
Increased pressure in forearm muscles due to trauma or fracture.
Muscles can die if not treated quickly; leads to permanent contracture.

*Winging of the Scapula*
From long thoracic nerve injury. Serratus anterior cannot hold scapula to ribcage.

*Volkmann’s Ischemic Contracture*
From brachial artery injury or supracondylar fracture.
Flexors shorten and hand remains in uncontrolled flexion."""

CLINICAL_TESTS = """*Tests*

*Allen’s Test*
Checks radial and ulnar artery patency in the hand.
Compress both arteries, have patient clench fist, then release one artery and watch hand color return.

*Tinel’s Sign*
Tap median nerve at wrist to check for carpal tunnel syndrome. Tingling indicates positive test.

*Phalen’s Maneuver*
Flex wrist fully for 60 seconds. Numbness or pain in median nerve distribution indicates carpal tunnel syndrome.

*Painful Arc Test*
Patient abducts arm. Pain between 60 and 120 degrees suggests supraspinatus tendonitis or partial tear.

*Subscapularis Impingement Test*
Internal rotation of humerus with arm elevated; pain indicates impingement under coracoid or acromion.

*Hand of Benediction*
Ask patient to make a fist. If index and middle fingers do not flex fully, indicates median nerve injury.

*Ulnar Claw*
Patient extends fingers. Ring and little fingers remain flexed due to ulnar nerve damage."""

# ---------------------------
# MENUS
# ---------------------------

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("🦴 Upper Limb Osteology"),
        KeyboardButton("🩺 Fascia / Vessels / Cutaneous Nerves"),
        KeyboardButton("💪 Muscles of the Upper Limb"),
        KeyboardButton("🤝 Joints of the Upper Limb"),
        KeyboardButton("📍 Major Landmarks"),
        KeyboardButton("🧠 Brachial Plexus"),
        KeyboardButton("🚑 Clinical Correlations"),
        KeyboardButton("📚 About Bot")
    )
    return markup

def osteology_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Clavicle"),
        KeyboardButton("Scapula"),
        KeyboardButton("Humerus"),
        KeyboardButton("Radius and Ulna"),
        KeyboardButton("Hand Bones"),
        KeyboardButton("⬅ Back")
    )
    return markup

def fascia_vessels_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Fascia"),
        KeyboardButton("Vessels"),
        KeyboardButton("Cutaneous Nerves"),
        KeyboardButton("⬅ Back")
    )
    return markup

def muscles_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Muscles of the Upper Arm"),
        KeyboardButton("Muscles of the Forearm"),
        KeyboardButton("Small Muscles of the Hand"),
        KeyboardButton("The Rotator Cuff (SITS)"),
        KeyboardButton("Vertebral Column Connections"),
        KeyboardButton("Thoracic Wall Connections"),
        KeyboardButton("Scapula to Humerus Connections"),
        KeyboardButton("⬅ Back")
    )
    return markup

def rotator_cuff_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Rotator Cuff Overview"),
        KeyboardButton("Supraspinatus"),
        KeyboardButton("Infraspinatus"),
        KeyboardButton("Teres Minor"),
        KeyboardButton("Subscapularis"),
        KeyboardButton("⬅ Back to Muscles")
    )
    return markup

def joints_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Shoulder Joint"),
        KeyboardButton("Elbow Joint"),
        KeyboardButton("Radioulnar Joints"),
        KeyboardButton("Wrist Joint"),
        KeyboardButton("Hand Joints"),
        KeyboardButton("⬅ Back")
    )
    return markup

def landmarks_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("The Axilla"),
        KeyboardButton("Cubital Fossa"),
        KeyboardButton("The Carpal Tunnel"),
        KeyboardButton("The Guyon's Canal"),
        KeyboardButton("The Anatomical Snuffbox"),
        KeyboardButton("⬅ Back")
    )
    return markup

def brachial_plexus_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Formation"),
        KeyboardButton("Roots (C5-T1)"),
        KeyboardButton("Trunks"),
        KeyboardButton("Divisions"),
        KeyboardButton("Cords"),
        KeyboardButton("Supraclavicular Branches"),
        KeyboardButton("Infraclavicular Branches"),
        KeyboardButton("Major Terminal Nerves"),
        KeyboardButton("⬅ Back")
    )
    return markup

def clinical_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Fractures"),
        KeyboardButton("Dislocations and Joint Injuries"),
        KeyboardButton("Nerve Injuries"),
        KeyboardButton("Vascular Injuries"),
        KeyboardButton("Muscle and Tendon Injuries"),
        KeyboardButton("Special Conditions"),
        KeyboardButton("Tests"),
        KeyboardButton("⬅ Back")
    )
    return markup

# ---------------------------
# HANDLERS
# ---------------------------

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "Welcome to *Joshua's Anatomy Bot*! 🦴\n\n"
        "I am your comprehensive guide to the *Anatomy of the Upper Limb*.\n"
        "Select a category below to start learning high-yield clinical information."
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text == "🦴 Upper Limb Osteology")
def show_osteology(message):
    bot.send_message(message.chat.id, "Select a bone to learn more:", reply_markup=osteology_menu())

@bot.message_handler(func=lambda message: message.text == "🩺 Fascia / Vessels / Cutaneous Nerves")
def show_fascia_vessels(message):
    bot.send_message(message.chat.id, "Select a topic:", reply_markup=fascia_vessels_menu())

@bot.message_handler(func=lambda message: message.text == "💪 Muscles of the Upper Limb")
def show_muscles(message):
    bot.send_message(message.chat.id, "Select a muscle group:", reply_markup=muscles_menu())

@bot.message_handler(func=lambda message: message.text == "The Rotator Cuff (SITS)")
def show_rotator_cuff(message):
    bot.send_message(message.chat.id, "Select a topic:", reply_markup=rotator_cuff_menu())

@bot.message_handler(func=lambda message: message.text == "🤝 Joints of the Upper Limb")
def show_joints(message):
    bot.send_message(message.chat.id, "Select a joint:", reply_markup=joints_menu())

@bot.message_handler(func=lambda message: message.text == "📍 Major Landmarks")
def show_landmarks(message):
    bot.send_message(message.chat.id, "Select a landmark:", reply_markup=landmarks_menu())

@bot.message_handler(func=lambda message: message.text == "🧠 Brachial Plexus")
def show_brachial_plexus(message):
    bot.send_message(message.chat.id, "Select a topic:", reply_markup=brachial_plexus_menu())

@bot.message_handler(func=lambda message: message.text == "🚑 Clinical Correlations")
def show_clinical(message):
    bot.send_message(message.chat.id, "Select a clinical section:", reply_markup=clinical_menu())

@bot.message_handler(func=lambda message: message.text == "📚 About Bot")
def about_bot(message):
    about_text = (
        "*Joshua's Anatomy Bot* 🦴\n\n"
        "This bot is designed for medical students and healthcare professionals "
        "to quickly review high-yield anatomical and clinical information about the upper limb.\n\n"
        "Created to provide 24/7 educational support."
    )
    bot.send_message(message.chat.id, about_text, parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == "⬅ Back")
def back_to_main(message):
    bot.send_message(message.chat.id, "Returning to Main Menu.", reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text == "⬅ Back to Muscles")
def back_to_muscles(message):
    bot.send_message(message.chat.id, "Returning to Muscles Menu.", reply_markup=muscles_menu())

@bot.message_handler(func=lambda message: True)
def handle_content(message):
    content_map = {
        "Clavicle": CLAVICLE,
        "Scapula": SCAPULA,
        "Humerus": HUMERUS,
        "Radius and Ulna": RADIUS_ULNA,
        "Hand Bones": HAND_BONES,
        "Fascia": FASCIA,
        "Vessels": VESSELS,
        "Cutaneous Nerves": CUTANEOUS_NERVES,
        "The Axilla": AXILLA,
        "Cubital Fossa": CUBITAL_FOSSA,
        "The Carpal Tunnel": CARPAL_TUNNEL,
        "The Guyon's Canal": GUYONS_CANAL,
        "The Anatomical Snuffbox": ANATOMICAL_SNUFFBOX,
        "Formation": BP_FORMATION,
        "Roots (C5-T1)": BP_ROOTS,
        "Trunks": BP_TRUNKS,
        "Divisions": BP_DIVISIONS,
        "Cords": BP_CORDS,
        "Supraclavicular Branches": BP_SUPRACLAVICULAR,
        "Infraclavicular Branches": BP_INFRACLAVICULAR,
        "Major Terminal Nerves": BP_TERMINAL,
        "Vertebral Column Connections": MUSCLES_VERTEBRAL,
        "Thoracic Wall Connections": MUSCLES_THORACIC,
        "Scapula to Humerus Connections": MUSCLES_SCAPULA_HUMERUS,
        "Muscles of the Upper Arm": MUSCLES_ARM_ANTERIOR + "\n\n" + MUSCLES_ARM_POSTERIOR,
        "Muscles of the Forearm": MUSCLES_FOREARM_ANTERIOR + "\n\n" + MUSCLES_FOREARM_POSTERIOR,
        "Small Muscles of the Hand": MUSCLES_HAND,
        "Shoulder Joint": JOINT_SHOULDER,
        "Elbow Joint": JOINT_ELBOW,
        "Radioulnar Joints": JOINT_RADIOULNAR,
        "Wrist Joint": JOINT_WRIST,
        "Hand Joints": JOINT_HAND,
        "Rotator Cuff Overview": ROTATOR_CUFF_OVERVIEW,
        "Supraspinatus": MUSCLE_SUPRASPINATUS,
        "Infraspinatus": MUSCLE_INFRASPINATUS,
        "Teres Minor": MUSCLE_TERES_MINOR,
        "Subscapularis": MUSCLE_SUBSCAPULARIS,
        "Fractures": CLINICAL_FRACTURES,
        "Dislocations and Joint Injuries": CLINICAL_DISLOCATIONS,
        "Nerve Injuries": CLINICAL_NERVES,
        "Vascular Injuries": CLINICAL_VASCULAR,
        "Muscle and Tendon Injuries": CLINICAL_MUSCLES,
        "Special Conditions": CLINICAL_SPECIAL,
        "Tests": CLINICAL_TESTS
    }
    
    if message.text in content_map:
        bot.send_message(message.chat.id, content_map[message.text], parse_mode="Markdown")
    elif message.text not in ["🦴 Upper Limb Osteology", "🩺 Fascia / Vessels / Cutaneous Nerves", "💪 Muscles of the Upper Limb", "🤝 Joints of the Upper Limb", "🚑 Clinical Correlations", "The Rotator Cuff (SITS)", "Rotator Cuff Overview", "Supraspinatus", "Infraspinatus", "Teres Minor", "Subscapularis", "Muscles of the Upper Arm", "Muscles of the Forearm", "Small Muscles of the Hand", "📍 Major Landmarks", "🧠 Brachial Plexus", "📚 About Bot", "⬅ Back", "⬅ Back to Muscles"]:
        bot.send_message(message.chat.id, "Please use the menu buttons to navigate.")

# ---------------------------
# RUN
# ---------------------------

if __name__ == '__main__':
    # Start Flask thread
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Start Bot
    print("Bot is running...")
    bot.infinity_polling()
