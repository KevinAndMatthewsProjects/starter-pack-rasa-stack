import java.util.*;
public class HealthAdvice {
	private Random rand = new Random();
	public String getHealthAdvice() {
		String[] advice = new String[]{
			"Limit the amount sugary beverages you drink to prevent obesity and diabetes.",
			"Nuts have high nutritional value and can help you lose weight.",
			"Try to avoid processed junk food since they have low nutritional value.",
			"The US Department of Health and Human Services recommends at least 150 minutes of "
			+ "moderate aerobic activity or 75 minutes of vigorous aerobic activity a week, or"
			+ "a combination of the two.", 
			"Prevent dehydration by drinking at least 2 liters of water everyday!",
			"Be sure to get at least 8 hours of sleep for an energized morning!",
			"Eat vegetables! They contain plenty of vitamins, minerals, and antioxidants!",
			"Avoid smoking to reduce risk of lung cancer.",
			"Reduce intake of red meats to prevent cholesterol buildup.",
			"Stay hydrated!" ,
			"Studies have shown that cutting down on sugary foods can greatly improve energy, mood, as well help with weight loss!" , 
			"Vaccines are essential for a long healthy life!",
			"Don't underestimate the effect of staying active! Just fifteen minutes a day can improve mood.",
			"A doctor a day can keep the apple away!",
			"An apple a day keeps the doctor away!" , 
			"Smoking is bad for one's health!",
			"Mental health is important! Reach out to others if you need help!",
			"Get tested!",
			"Keep your head up!"
			"Protection is key!",
			"Don't trust everything you read online! (Including me!)",
			"Power naps can reduce stress and help people regain energy! 30 minute naps are recommended",
			"Don't ask doctors for antibiotics every time you are sick! The drugs kill good and bad bacteria indiscrimminately and can lead to drug resistant bacteria!",
			"Always wear a helmet while biking or boarding!",
			"Always buckle your seatbelts!"
 
		};
		return advice[rand.nextInt(advice.length)];
	}
	
	public static void main(String[] args) {
		HealthAdvice health = new HealthAdvice();
		System.out.println(health.getHealthAdvice());
	}
}
